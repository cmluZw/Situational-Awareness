import time

from model.apache import Apache
from model.network import Network

def timehandle(time1):
    # 先转换为时间数组
    timeArray = time.strptime(time1, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳
    otherStyleTime = time.strftime("%H:%M:%S", timeArray)
    print(otherStyleTime)
    return otherStyleTime

# timehandle("2022-02-10 11:57:04")

def selectevent():
    apache=Apache()
    network=Network()
    apache_list = apache.query.all()
    network_list = network.query.all()
    ip_list=list()
    time_list=list()
    type_list=list()
    for i in apache_list:
        ip_list.append(i.ip)
        time_list.append(timehandle(i.time))
        type_list.append(i.attack_type)
    for i in network_list:
        ip_list.append(i.srcip)
        time_list.append(timehandle(i.time))
        type_list.append(i.attack_type)
    # print(ip_list,time_list,type_list)

    for i in range(0,len(ip_list)):
        if type_list[i] == '101':
            type_list[i]='XSS跨站'
        elif type_list[i] == '102':
            type_list[i] = 'SQL注入'
        elif type_list[i] == '103':
            type_list[i] = '目录扫描'
        elif type_list[i] == '104':
            type_list[i] = 'DoS攻击'
        elif type_list[i] == '105':
            type_list[i] = '暴力破解'
        elif type_list[i] == '106':
            type_list[i] = '木马后门'
        elif type_list[i] == '107':
            type_list[i] = 'SSH爆破'
        else:
            type_list[i] = '暂无威胁'

    return ip_list,time_list,type_list
    # print(ip_list,time_list,type_list)
# selectevent()


