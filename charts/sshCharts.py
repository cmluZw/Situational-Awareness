import json

from pyecharts import Line,Pie,Grid,Gauge
from model.ssh import Ssh
import admin.ipanalyse as ipanalyse

def selectssh():
    ssh=Ssh()
    ssh_list = ssh.query.all()
    ip_list=list()
    num_list=list()
    for i in ssh_list:
        ip_list.append(i.ip)
        num_list.append(i.num)
    return ip_list,num_list

# def sshLineCharts():#ssh攻击统计折线图
#     ip_list,num_list=selectssh()
#     ssh_line=Line("Ssh爆破攻击趋势图")
#     ssh_line.add('Ssh爆破攻击趋势',ip_list,num_list,is_show=True)
#     # ssh_line.render()
#     ssh_line.chart_id="ssh_line"
#     ssh_line.render()
#     # return ssh_line

def sshPieCharts():
    ip_list, num_list = selectssh()
    grid = Grid(width="250px", height="250px")
    ssh_pie=Pie()
    ssh_pie.add("ssh爆破统计", ip_list, num_list, radius=[28, 38], label_text_color=None,
            legend_orient='vertical', center=[15, 25], is_legend_show=False, is_toolbox_show=False,
            is_label_show=False,label_color=['#8080C0','#007979', '#97CBFF',  '#2894FF', '#E8FFC4','#CDCD9A','#C4E1E1','#4A4AFF','#2894FF','#AAAAFF','#4DFFFF','#9D9D9D'])
    # ssh_pie.render()
    ssh_sum=0
    for i in num_list:
        ssh_sum+=int(i)
    # print(ssh_sum)
    with open('./output/analyse/network/flowStatistics.txt', 'r') as fp:
        streams = json.load(fp)
        val = list(streams.values())
        stream_in=0
        for v in val:
            stream_in+=v[0]
        # print(stream_in)
    risk=ssh_sum/stream_in
    # risk_index_pannel='{:.2f}'.format(risk*100)
    risk_index='{:.0%}'.format(risk)
    # gauge = Gauge()
    # gauge.add("", "", risk_index_pannel,is_toolbox_show=False,radius="50%")
    # # gauge.show_config()
    # grid.add(gauge,grid_top="10px")
    return ssh_pie,risk_index
# sshPieCharts()
