'''写恶意事件管理+原始数据管理'''
import os

import config
from model.network import Network
from admin import networkbyipanalyse

def getraw_data(ip):#通过ip各日志和流量数据查找溯源
    print(ip)
    #从apache日志里溯源
    apache_raw=[]
    cmd="cat {0} | grep {1}" .format(config.apache_log,ip)
    stream = os.popen(cmd)
    output = stream.read().split()
    stream.close()
    if output:
        for i in output:
            apache_raw.append(i)
    else:
        pass
    #从ssh日志里溯源
    ssh_raw=[]
    cmd="lastb | grep {0}" .format(ip)
    stream = os.popen(cmd)
    output = stream.read().split()
    stream.close()
    if output:
        for i in output:
            ssh_raw.append(i)
    else:
        pass
    # 从流量包里溯源
    network_raw=[]
    network=Network()
    network.srcip=ip
    raw_request_list=network.selectbyip()
    for i in raw_request_list:
        network_raw.append(i)
    print(network_raw)
    return apache_raw,ssh_raw,network_raw


def getpktby_ip(ip):
    networkbyipanalyse.networkanalyse(ip)





# getraw_data('101.33.228.166')