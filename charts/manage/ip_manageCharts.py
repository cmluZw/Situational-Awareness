import json
from pyecharts import Line,Pie,Grid
import admin.manage.ip_manage as ip_manage


def ip_mamange_PieCharts():
    ip_list, num_list = selectssh()
    grid = Grid(width="100%", height="100%")
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
    risk_index='{:.0%}'.format(risk)
    return ssh_pie,risk_index
# sshPieCharts()