'''写恶意事件管理+原始数据管理'''
import os

import config
from model.network import Network
from admin import networkbyipanalyse
from model.apache import Apache
from model.ssh import  Ssh

def getraw_data(ip):#通过ip各日志和流量数据查找溯源
    print(ip)
    #从apache日志里溯源
    apache_raw=[]
    cmd="cat {0} | grep {1}" .format(config.apache_log,ip)
    stream = os.popen(cmd)
    output = stream.read().split()
    stream.close()
    if output:
        print("output: " + str(output))
        apache_raw.append(str(output))
    #        for i in output:
    #            apache_raw.append(str(i))

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
            ssh_raw.append(str(i))
    else:
        pass
    # 从流量包里溯源
    network_raw=[]
    network=Network()
    network.srcip=ip
    raw_request_list=network.selectbyip()
    for i in raw_request_list:
        network_raw.append(str(i))
    print(network_raw)
    return apache_raw,ssh_raw,network_raw

def selectevent_byip(ip):
    apache=Apache()
    ssh=Ssh()
    network=Network()
    apache.ip=ip
    ssh.ip=ip
    network.srcip=ip
    event_num={'XSS跨站':0,'SQL注入':0,'目录扫描':0,'DoS攻击':0,'暴力破解':0,'木马后门':0,'SSH爆破':0}
    apache_list=apache.selectevent_byip()
    network_list=network.selectevent_byip()
    event_list=apache_list+network_list
    ssh_list=ssh.selectevent_byip()
    for i in event_list:
        if i.attack_type=='101':
            event_num['XSS跨站']+=1
        if i.attack_type=='102':
            event_num['SQL注入']+=1
        if i.attack_type=='103':
            event_num['目录扫描']+=1
        if i.attack_type=='104':
            event_num['DoS攻击']+=1
        if i.attack_type=='105':
            event_num['暴力破解']+=1
        if i.attack_type=='106':
            event_num['木马后门']+=1
        if i.attack_type=='107':
            event_num['SSH爆破']+=1
    for i in ssh_list:
        event_num['SSH爆破'] += int(i.num)
#     print(event_num)
    return event_num

# selectevent_byip("101.33.228.166")

def getpktby_ip(ip):
    networkbyipanalyse.networkanalyse(ip)





# getraw_data('101.33.228.166')