from time import strftime

from admin.manage import dangerous_manage
from model.danger import Danger
from admin.manage import defend

def selectdanger():
    danger=Danger()
    danger_list = danger.query.all()
    ip_list=list()
    time_list=list()
    is_deal_list=list()
    for i in danger_list:
        ip_list.append(i.ip)
        time_list.append(i.time)
        is_deal_list.append(i.is_deal)
    print(ip_list,time_list,is_deal_list)
    return ip_list,time_list,is_deal_list


def dealdanger():#防御
    ip_list, time_list, is_deal_list=selectdanger()
    for i in range(0,len(ip_list)):
        if is_deal_list[i]==0:
            result=defend.defend(ip_list[i])
            if result==1:
                print("ip: {} 防御失败".format(ip_list[i]))
            elif result==0:
                deal=dangerous_manage.dealdanger(ip_list[i])
                print("已自动防御ip为: {} 的攻击".format(ip_list[i]))
            else:
                print("ip: {} 防御失败".format(ip_list[i]))
        else:
            pass



# dealdanger()