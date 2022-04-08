from time import strftime

from scapy.all import *
from model.raw_data import Raw_data
import config

def handelPacket(pkt):  # pkt捕获到的数据包
    data=0
    srcip=""
    if pkt.haslayer('TCP') and pkt.haslayer('Raw'):  # 读取传输层和应用层
        if pkt['TCP']:
            print("tcp")
            load=pkt['Raw'].load
            s=tostr(load, pkt)
            data=handels(s)
            srcip = pkt["IP"].src
    elif pkt.haslayer('ICMP'):
        # pkt.show()
        print("icmp")
        load = pkt['ICMP'].load
        data=tostr(load, pkt)
        srcip = pkt["IP"].src
    if data!=0:
        raw_data = Raw_data()
        raw_data.srcip = srcip
        raw_data.dstip = config.local_ip
        raw_data.raw_request = data
        raw_data.time=strftime('%m/%d %H:%m')
        raw_data.insert()
    else:
        print("无数据")




def tostr(load, pkt):
    '''HTTP 流量分析'''
    # byte 转 str
    try:
        s = str(load.decode())
    except:
        s = str(load)
        if s[:2] == "b'":
            s = s[2:-1]
    print(s)
    return s

def handels(s):
    if 'GET /' in s[:10]:
        return s
    elif 'POST /' in s[:10]:
        return s
    else:
        return 0



def networkanalyse(ip):
    # pkt = sniff(filter='ip dst {} and ip src {}'.format(config.local_ip, config.local_ip),prn=flowanalyse)
    pkt=sniff( filter="ip src ".format(ip), prn=handelPacket,count=0)

# networkanalyse("10.13.138.84")