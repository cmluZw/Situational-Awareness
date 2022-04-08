import json
from socket import gethostname, gethostbyname
from time import ctime, strftime
from urllib.parse import unquote

from scapy.all import *
from model.network import Network
import config
import admin.ipanalyse as ipanalyse
from model.raw_data import Raw_data


def evilAnalyse(args):
    #恶意流量分析
    try:
        #多参数
        if '&' in args and '=' in args:
            args = args.split('&')
            # 单参数
        elif '=' in args and '&' not in args:
            args = [args]
            # 上传文件时的文件参数
        elif 'boundary=----' in args:
            args = [args]
            # 无参数
        else:
            return 0, 100
        for param in args:
            # 提取参数值
            indx = param.index('=')
            value = param[indx + 1:]
            value = unquote(value).lower()
            # SQL 注入判断
            rule = config.sqlrule
            for i in rule:
                if i in value:
                    return 1, 102
            # XSS 判断
            rule = config.xssrule
            for i in rule:
                if i in value:
                    return 1, 101
            # 木马后门判断
            rule = config.backrule
            for i in rule:
                if i in value:
                    return 1, 106
        return 0, 100
    except Exception as e:
        con = ctime() + ' ' + str(e)
        with open('./output/analyse/network/error_log.log', 'a+') as ef:
            ef.write(con + '\n')#记录日志报错
        return 0, 100


def httpAnalyse(load, pkt):
    '''HTTP 流量分析'''
    # byte 转 str
    try:
        s = str(load.decode())
    except:
        s = str(load)
        if s[:2] == "b'":
            s = s[2:-1]
    # print(s)
    # 分析 POST 请求
    if 'POST /' in s[:10]:
        try:
            type = 'POST'
            srcIP = pkt["IP"].src
            tmpVar = s.split('\r\n\r\n')
            tmpFile = s.split(' HTTP/1')[0]
            tfile = tmpFile[5:]
            # 有参数
            if len(tmpVar) > 1:
                args = tmpVar[1]
                isEvil, evilType = evilAnalyse(args)
            # 无参数
            else:
                args = ''
                isEvil, evilType = 0, 100

            time = strftime('%m/%d %H:%m')
            network=Network()
            network.attack_type=evilType
            network.srcip=srcIP
            network.time=time
            network.raw_request=s

            if network.attack_type != 100:#存在威胁
                network.insert()
                ipanalyse.seperate_ip(network.get_srcip())#分析来源ip

        except Exception as e:
            con = ctime() + ' ' + str(e)
            with open('./output/analyse/network/error_log.log', 'a+') as ef:
                ef.write(con + '\n') #同样写入日志错误信息
            pass
    # 分析 GET 请求
    elif 'GET /' in s[:10]:
        try:
            type = 'GET'
            srcIP = pkt["IP"].src
            tmpVar = s.split(' HTTP/1')[0]
            indx = tmpVar.find('?')
            # 无参数
            if indx == -1:
                args = ''
                isEvil, evilType = 0, 100
                tfile = tmpVar[4:]
            # 有参数
            else:
                args = tmpVar[indx + 1:]
                isEvil, evilType = evilAnalyse(args)
                tfile = tmpVar[4:indx]
            time = strftime('%m/%d %H:%m')

            network = Network()
            network.attack_type = evilType
            network.srcip = srcIP
            network.time = time
            network.raw_request = s

            if network.attack_type != 100:
                network.insert()
                ipanalyse.seperate_ip(network.get_srcip())  # 分析来源ip
        except Exception as e:
            con = ctime() + ' ' + str(e)
            with open('./output/analyse/network/error_log.log', 'a+') as ef:
                ef.write(con + '\n')
            pass

def flowanalyse(pkt):
    '''对每个数据包进行分析'''
    # 进出口流量统计
    # host = gethostname()
    # ip = gethostbyname(host) #这样自动绑定的是以太网信息，如果是wifi就无法捕获流量
    ip=config.local_ip
    network = Network()
    if ip == pkt['IP'].dst: #入口流量
        network.trafficIn += len(pkt)
        # 仅分析入站流量
        # 判断是否是带有数据的 TCP 数据包
        if pkt.haslayer('TCP') and pkt.haslayer('Raw'):#读取传输层和应用层
            # 如果是 HTTP 则传入 analyse 函数对内容进行分析
            if pkt['TCP']:
                load = pkt['Raw'].load
                httpAnalyse(load, pkt)
        # 判断是否是 Ping of Death
        elif pkt.haslayer('ICMP') and len(pkt) > 1400:
            time = strftime('%m/%d %H:%m')
            network.srcip=pkt['IP'].src
            network.attack_type=104
            network.time=time
            network.insert()
    else:
        network.trafficOut += len(pkt)
    # 在整点时统计出入站流量
    now_time = strftime('%H:00')
    # print(now_time)
    if now_time in network.tmp_time:
        network.tmp_time.remove(now_time)
        # 如在 13 点则统计的是 12 点的流量, 0 点则统计 23 点的流量
        if now_time == '00:00':
            check_time = '23:00'
        else:
            check_time = '{:0>2d}:00'.format(int(now_time[:2]) - 1)
        # print(network.trafficIn // config.stream_unit)
        # print(network.trafficOut // config.stream_unit)
        network.all_time[check_time] = [
            network.trafficIn // config.stream_unit, network.trafficOut // config.stream_unit]
        print(network.all_time[check_time])
        if check_time == '00:00':
            for otime in network.all_time:
                if otime != '00:00':
                    network.all_time[otime] = [0, 0]
        # network.trafficIn = 0
        # network.trafficOut = 0 #因为我直接传的是model，并不是self，所以不需要每次都初始化为0
        # print(network.all_time)
        # with open('./output/stream_status.log', 'w') as f:
        #     f.write(network.all_time)
        with open('./output/analyse/network/flowStatistics.txt', 'a') as f:
            f.write(json.dumps(network.all_time))
    if network.tmp_time == []:
        network.tmp_time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
                               '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                               '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        network.tmp_time.remove(now_time)

def networkanalyse():
    # pkt = sniff(filter='ip dst {} and ip src {}'.format(config.local_ip, config.local_ip),prn=flowanalyse)
    pkt = sniff(filter='ip dst {} or ip src {}'.format(config.local_ip, config.local_ip),prn=flowanalyse)

# networkanalyse()