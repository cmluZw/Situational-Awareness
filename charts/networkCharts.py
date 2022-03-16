import json

from pyecharts import Pie, Grid, Line

from model.network import Network


def selectnetworkinfo():
    network=Network()
    network_list = network.query.all()
    srcip_list=list()
    dstip_list=list()
    attack_type_list=list()
    raw_request_list=list()
    for i in network_list:
        srcip_list.append(i.srcip)
        dstip_list.append(i.dstip)
        attack_type_list.append(i.attack_type)
        raw_request_list.append(i.raw_request)
    return srcip_list,dstip_list,attack_type_list,raw_request_list

def networkcharts():#存在威胁的ip已经放进世界地图里，这里统计攻击类型
    srcip_list, dstip_list, attack_type_list, raw_request_list=selectnetworkinfo()
    length=len(srcip_list)
    columns=[
        'XSS跨站',
        'SQL注入',
        'DoS攻击',
        '木马后门',
    ]
    data = [0, 0, 0, 0]
    for i in range(length):  # 统计，将类型相同的num加在一起存入data
        if int(attack_type_list[i]) == 101:
            data[0] = data[0] + 1
        if int(attack_type_list[i]) == 102:
            data[1] = data[1] + 1
        if int(attack_type_list[i]) == 104:
            data[2] = data[2] + 1
        if int(attack_type_list[i]) == 106:
            data[3] = data[3] + 1

    for i in data:
        print(i)

    pie = Pie()
    pie.add("流量分析统计", columns, data, radius=[28, 38], label_text_color=None,
            legend_orient='vertical', center=[10, 20], is_legend_show=False, is_toolbox_show=False,
            is_label_show=True,label_pos='center',label_color=['#8080C0','#007979', '#97CBFF',  '#2894FF'])

    # pie.render()#测试完成
    pie.chart_id = 'network_pie'
    return pie

def streamcharts(): #流量统计
    with open('./output/analyse/network/flowStatistics.txt', 'r') as fp:
        streams = json.load(fp)
    print(streams)
    stream_time = list(streams.keys())
    val = list(streams.values())
    stream_in = [v[0] for v in val]
    stream_out = [v[1] for v in val]
    print(stream_in,stream_out)
    grid = Grid(width="100%", height="100%")
    stream = Line()
    stream.add("入口流量", stream_time, stream_in, is_fill=True, line_opacity=1,
               line_color="#FFD700", label_color=["#FFD700", "#6A6AFF"],
               area_opacity=0.7, is_smooth=True, is_toolbox_show=False, is_yaxis_show=False)
    stream.add("出口流量", stream_time, stream_out, is_fill=True, area_color='#000',
               area_opacity=0.4, is_smooth=True, is_toolbox_show=False, is_yaxis_show=False,
               is_legend_show=True, legend_text_color="#46A3FF", xaxis_line_color="#4169E1")
    # stream.add("入口流量", stream_time, stream_in, is_fill=True, line_opacity=1,is_smooth=True, is_toolbox_show=False, is_yaxis_show=False)
    # stream.add("出口流量", stream_time, stream_out, is_fill=True, is_smooth=True, is_toolbox_show=False, is_yaxis_show=False)
    grid.add(stream, grid_bottom=30, grid_left=30, grid_top=50, grid_right=30)
    # grid.render()
    return grid

streamcharts()