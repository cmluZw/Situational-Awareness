from pyecharts import Pie
from model.apache import Apache

def selectapache():
    apache=Apache()
    apache_list=apache.query.all()
    ip_list=list()
    num_list=list()
    type_list=list()
    for i in apache_list:
        ip_list.append(i.ip)
        num_list.append(i.num)
        type_list.append(i.attack_type)
    return ip_list,num_list,type_list
    # print(ip_list,num_list,type_list)

def apachePieCharts():
    ip_list,num_list,type_list=selectapache()
    length=len(ip_list)
    columns=[
        'XSS跨站',
        'SQL注入',
        '目录扫描',
        'DoS攻击',
        '暴力破解',
    ]
    data=[0,0,0,0,0]
    for i in range(length):#统计，将类型相同的num加在一起存入data
        if int(type_list[i])==101:
            data[0]=data[0]+int(num_list[i])
        if int(type_list[i])==102:
            data[1]=data[1]+int(num_list[i])
        if int(type_list[i])==103:
            data[2]=data[2]+int(num_list[i])
        if int(type_list[i])==104:
            data[3]=data[3]+int(num_list[i])
        if int(type_list[i])==105:
            data[4]=data[4]+int(num_list[i])
        # if int(type_list[i])==6:  #ssh爆破
        #     data[5]=data[5]+int(num_list[i])
        # if int(type_list[i])==7:  #木马后门 这俩不属于apache日志里面
        #     data[6]=data[6]+int(num_list[i])
    # for i in data:
    #     print(i)
    pie=Pie()
    # pie.add("apache日志分析统计",columns,data,center=[75,50],is_legend_show=False,is_label_show=True,radius = ["15%", "20%"])
    pie.add("apache日志分析统计",columns,data,radius=[28, 38], label_text_color=None,
               legend_orient='vertical', center=[10, 20], is_legend_show=False, is_toolbox_show=False,
               is_label_show=False,label_color=['#8080C0','#007979', '#97CBFF',  '#003E3E', '#2894FF'])
    # pie.render()

    pie.chart_id='apache_pie'
    return pie

# apachePieCharts()