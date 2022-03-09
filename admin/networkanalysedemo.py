# -*- coding:utf-8 -*-
from scapy.all import sniff
from time import strftime, ctime
from urllib.parse import unquote
from socket import gethostbyname, gethostname
import config
import json


class netCapture:
    # 入口流量
    trafficIn = 0
    # 出口流量
    trafficOut = 0
    # 时间:流量
    all_time = {'00:00': [0, 0], '01:00': [0, 0], '02:00': [0, 0], '03:00': [0, 0], '04:00': [0, 0], '05:00': [0, 0],
                '06:00': [0, 0], '07:00': [0, 0], '08:00': [0, 0], '09:00': [0, 0], '10:00': [0, 0], '11:00': [0, 0],
                '12:00': [0, 0], '13:00': [0, 0], '14:00': [0, 0], '15:00': [0, 0], '16:00': [0, 0], '17:00': [0, 0],
                '18:00': [0, 0], '19:00': [0, 0], '20:00': [0, 0], '21:00': [0, 0], '22:00': [0, 0], '23:00': [0, 0],
                }
    # 辅助变量
    tmp_time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                '22:00', '23:00']

    def __init__(self, filter='ip dst {} and ip src {}'.format(config.local_ip, config.local_ip), iface=config.local_adapter, count=0):
        self.filter = filter
        self.iface = iface
        self.count = count

    def evilAnalyse(self, args):
        '''恶意流量判断'''
        try:
            # HTTP 参数分割
            # 多参数
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
            with open('./output/error_log.log', 'a+') as ef:
                ef.write(con + '\n')
            return 0, 100

    def httpAnalyse(self, load, pkt):
        '''HTTP 流量分析'''
        # byte 转 str
        try:
            s = str(load.decode())
        except:
            s = str(load)
            if s[:2] == "b'":
                s = s[2:-1]
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
                    isEvil, evilType = self.evilAnalyse(args)
                # 无参数
                else:
                    args = ''
                    isEvil, evilType = 0, 100

                time = strftime('%m/%d %H:%m')
                info = {
                    'type': type,
                    'srcIP': srcIP,
                    'args': args,
                    'isEvil': isEvil,
                    'evilType': evilType,
                    'time': time,
                    'content': s
                }
                req = {
                    srcIP: isEvil
                }
                with open('./output/requests_ip.log', 'a+') as f:
                    f.write(json.dumps(req) + '\n')
                if isEvil:
                    evillink = [srcIP, tfile, evilType]
                    with open('./output/analyse/http_analyse', 'a+') as f:
                        f.write(json.dumps(info) + '\n')
                    with open('./output/evillink_status.log', 'a') as f:
                        f.write(json.dumps(evillink) + '\n')
            except Exception as e:
                con = ctime() + ' ' + str(e)
                with open('./output/error_log.log', 'a+') as ef:
                    ef.write(con + '\n')
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
                    isEvil, evilType = self.evilAnalyse(args)
                    tfile = tmpVar[4:indx]
                time = strftime('%m/%d %H:%m')
                info = {
                    'type': type,
                    'srcIP': srcIP,
                    'args': args,
                    'isEvil': isEvil,
                    'evilType': evilType,
                    'time': time,
                    'content': s
                }
                req = {
                    srcIP: isEvil
                }
                with open('./output/requests_ip.log', 'a+') as f:
                    f.write(json.dumps(req) + '\n')
                if isEvil:
                    evillink = [srcIP, tfile, evilType]
                    with open('./output/analyse/http_analyse', 'a+') as f:
                        f.write(json.dumps(info) + '\n')
                    with open('./output/evillink_status.log', 'a') as f:
                        f.write(json.dumps(evillink) + '\n')
            except Exception as e:
                con = ctime() + ' ' + str(e)
                with open('./output/error_log.log', 'a+') as ef:
                    ef.write(con + '\n')
                pass

    def analyse(self, pkt):
        '''对每个数据包进行分析'''
        # 进出口流量统计
        host = gethostname()
        ip = gethostbyname(host)
        if ip == pkt['IP'].dst:
            netCapture.trafficIn += len(pkt)
            # 仅分析入站流量
            # 判断是否是带有数据的 TCP 数据包
            if pkt.haslayer('TCP') and pkt.haslayer('Raw'):
                # 如果是 HTTP 则传入 analyse 函数对内容进行分析
                if pkt['TCP'].dport == 80:
                    load = pkt['Raw'].load
                    self.httpAnalyse(load, pkt)
            # 判断是否是 Ping of Death
            elif pkt.haslayer('ICMP') and len(pkt) > 1400:
                time = strftime('%m/%d %H:%m')
                info = {
                    'type': 'PING',
                    'srcIP': pkt['IP'].src,
                    'isEvil': 1,
                    'evilType': 104,
                    'time': time,
                }
                evillink = [pkt['IP'].src, '', 104]
                with open('./output/analyse/icmp_analyse', 'a+') as f:
                    f.write(json.dumps(info) + '\n')
                with open('./output/evillink_status.log', 'a') as f:
                    f.write(json.dumps(evillink) + '\n')
        else:
            netCapture.trafficOut += len(pkt)
        # 在整点时统计出入站流量
        now_time = strftime('%2H:00')
        if now_time in netCapture.tmp_time:
            netCapture.tmp_time.remove(now_time)
            # 如在 13 点则统计的是 12 点的流量, 0 点则统计 23 点的流量
            if now_time == '00:00':
                check_time = '23:00'
            else:
                check_time = '{:0>2d}:00'.format(int(now_time[:2]) - 1)

            netCapture.all_time[check_time] = [
                netCapture.trafficIn // config.stream_unit, netCapture.trafficOut // stream_unit]
            if check_time == '00:00':
                for otime in netCapture.all_time:
                    if otime != '00:00':
                        netCapture.all_time[otime] = [0, 0]
            netCapture.trafficIn = 0
            netCapture.trafficOut = 0
            with open('./output/stream_status.log', 'w') as f:
                f.write(json.dumps(netCapture.all_time))
        if netCapture.tmp_time == []:
            netCapture.tmp_time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
                                   '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                                   '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
            netCapture.tmp_time.remove(now_time)

    def capture(self):
        '''
        利用 sniff 进行抓包并分析
        filter : 抓包过滤器
        iface  : 网卡
        prn    : 分析函数
        timeout: 抓包时长
        '''
        pkt = sniff(filter=self.filter, iface=self.iface,
                    prn=self.analyse, count=self.count)




