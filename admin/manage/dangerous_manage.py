'''写告警程序+防御'''
import os
from time import strftime

from charts import apacheCharts,networkCharts
from model.ssh import Ssh
from model.danger import Danger

def getsuccesslogin():
    cmd="last | awk '{print $3}'"
    stream = os.popen(cmd)
    # 获取执行结果
    output = stream.read().split()
    stream.close()
    successlogin=[]
    for i in output:
        # print(i)
        successlogin.append(i)
    print(successlogin)
    return successlogin

def selectsship():
    ssh=Ssh()
    ssh_list = ssh.query.all()
    ip_list=[]
    for i in ssh_list:
        item=i.ip.split('\n') #做格式处理
        # print(item[0])
        ip_list.append(item[0])
    # print(ip_list)
    return ip_list

def sshcheck():

    # successlogin=getsuccesslogin()
    ip_list=selectsship()
    danger_index = 0
    danger_list=[]
    successlogin=['101.43.67.184', '117.173.86.8', '117.173.86.8', '117.173.86.8', '159.223.29.20', '2.56.56.31', '91.239.130.201', '223.113.52.38', '117.173.86.10', '117.173.86.11', '117.173.86.11', '117.173.86.11', '117.173.86.8', '86.236.215.173', '117.173.86.11', '117.173.86.8']
    for i in ip_list:
        if i in successlogin:
            # print("找到i: "+i)
            danger_index = 1
            danger_list.append(i)
        else:
            pass
    # print(danger_list,danger_index)
    return danger_index,danger_list

def httpcheck():
    danger_index = 0
    danger_list=[]
    ip_list,num_list,type_list=apacheCharts.selectapache()
    srcip_list, dstip_list, attack_type_list, raw_request_list=networkCharts.selectnetworkinfo()

    for i in range(0,len(ip_list)):
        if type_list[i]==106:
            danger_index=1
            danger_list.append(ip_list[i])
        else:
            pass

    for i in range(0,len(srcip_list)):
        if attack_type_list[i]=='106':
            danger_index=1
            danger_list.append(srcip_list[i])
        else:
            pass

    print(danger_index,danger_list)
    return danger_index,danger_list

def check():
    danger_index1,danger_list1=sshcheck()
    danger_index2, danger_list2=httpcheck()
    danger_index = danger_index1 if danger_index1==0 else danger_index2
    danger_list=danger_list1+danger_list2
    if danger_index:
        # for i in danger_list:
        #     danger=Danger()
        #     danger.ip=i
        #     danger.time=strftime("%H:%M:%S")
        #     danger.insert()
        return danger_list
    else:
        return 0

# def danger():
#     check()


def dealdanger(ip):
    danger=Danger()
    danger.ip=ip
    try:
        data=danger.deal()
    except:
        data=0
    print(data)
    return data

def getis_deal(ip):
    danger=Danger()
    danger.ip=ip
    danger_index=0
    try:
        is_deal_list=danger.selectbyip()
        for i in is_deal_list:
            if i.is_deal==1:
                danger_index=1
            else:
                pass
    except:
        danger_index=0
    print(danger_index)
    return danger_index


def danger():
    danger_list=check()

    for i in danger_list:
        danger_index = getis_deal(i)
        if danger_index:#已经被处理
            pass
        else:
            print("自动防御存储中....")
            danger=Danger()
            danger.ip=i
            danger.time=strftime("%H:%M:%S")
            danger.insert()










