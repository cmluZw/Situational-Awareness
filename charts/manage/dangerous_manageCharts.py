from time import strftime

from admin.manage import dangerous_manage
from model.danger import Danger
from admin.manage import defend
from pyecharts import Bar, Grid, Page, Line
import admin.manage.defend

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

def selectisdeal(ip):
    danger=Danger()
    danger.ip=ip
    data_list=danger.getisdeal()
    for i in data_list:
        if i.is_deal == 1:  #已经被处理
            return 1
        else:
            pass
    return 0

def dealdanger():#被动防御/自动防御
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

def dealdangerbyself(ip):  #手动防御/主动防御

    defendresult=defend.defend(ip)    #防御
    if defendresult==1: #防御失败
        print(ip+" 防御失败")
        return 0
    result = dangerous_manage.dealdanger(ip)  # 修改数据库
    if result==0:
        return 0 #错误
    else:
        return 1


def dangerBarCharts():
    danger=Danger()
    data_list=danger.isdealStatistics()
    # 成功防御
    is_deal_ip_list,is_deal_num_ip,not_deal_ip_list,not_deal_num_ip=[],[],[],[]
    for i in data_list:
        is_deal_ip_list.append(i.ip)
        is_deal_num_ip.append(i.num)
    print(is_deal_ip_list,is_deal_num_ip)

    # 防御失败
    not_data_list=danger.notdealStatistics()
    for i in not_data_list:
        not_deal_ip_list.append(i.ip)
        not_deal_num_ip.append(i.num)
    print(not_deal_ip_list,not_deal_num_ip)
    bar = Bar("")
    bar.add("防御成功", is_deal_ip_list, is_deal_num_ip, is_label_show=False,is_legend_show=False, is_toolbox_show=False,is_xaxis_show=False,is_yaxis_show= False,label_color=['#007979'],is_convert=True)
    bar.add("防御失败", not_deal_ip_list, not_deal_num_ip,is_label_show=False,is_legend_show=False, is_toolbox_show=False,is_xaxis_show=False,is_yaxis_show= False,label_color=['#CDCD9A'],is_convert=True)
    # bar.render()
    grid = Grid(width="25%", height="400px")
    grid.add(bar,grid_top=0,)
    #
    # return page
    # grid.render()
    return grid
# dangerBarCharts()
# dealdanger()