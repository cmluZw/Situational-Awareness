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
    pie.add("流量分析统计", columns, data, radius=[30, 38], label_text_color=None,
            legend_orient='vertical', center=[50, 60], is_legend_show=False, is_toolbox_show=False,
            is_label_show=False)
    # pie.render()#测试完成
    pie.chart_id = 'network_pie'
    return pie

def streamcharts(): #流量统计
    with open('../output/analyse/network/flowStatistics.txt', 'r') as fp:
        streams = json.load(fp)
    print(streams)
    stream_time = list(streams.keys())
    val = list(streams.values())
    stream_in = [v[0] for v in val]
    stream_out = [v[1] for v in val]
    print(stream_in,stream_out)
    grid = Grid(width="100%", height="100%")
    stream = Line('    进出口流量统计\n    -------------------', width="100%", height="100%",
                  title_color="#6cb7c9", title_pos="left", title_top=10)
    stream.add("入口流量", stream_time, stream_in, is_fill=True, line_opacity=1,
               line_color="#6cb7c9", label_color=["#6cb7c9", "#344356"],
               area_opacity=0.7, is_smooth=True, is_toolbox_show=False, is_yaxis_show=False)
    stream.add("出口流量", stream_time, stream_out, is_fill=True, area_color='#000',
               area_opacity=0.4, is_smooth=True, is_toolbox_show=False, is_yaxis_show=False,
               is_legend_show=True, legend_text_color="#6cb7c9", xaxis_line_color="#6cb7c9")

    grid.add(stream, grid_bottom=30, grid_left=30, grid_top=50, grid_right=30)
    grid.render()

streamcharts()
# def stream_status(streams, is_reload=0):
#     grid = Grid(width="100%", height="100%")
#
#     # stream_time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
#     #                '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
#     #                '22:00', '23:00', '24:00']
#     # stream_in = [13, 6, 22, 5, 58, 3, 75, 98, 48, 83, 8, 38, 89, 99, 8, 21, 77, 86, 47, 76, 31, 92, 77, 47, 0]
#     # stream_out = [5, 81, 99, 83, 55, 89, 58, 5, 38, 76, 46, 17, 68, 4, 12, 81, 2, 73, 54, 71, 50, 28, 90, 46, 0]
#
#     stream_time = list(streams.keys())
#     val = list(streams.values())
#     stream_in = [v[0] for v in val]
#     stream_out = [v[1] for v in val]
#
#     stream = Line('    进出口流量统计\n    -------------------', width="100%", height="100%",
#                   title_color="#6cb7c9", title_pos="left", title_top=10)
#     stream.add("入口流量", stream_time, stream_in, is_fill=True, line_opacity=1,
#                line_color="#6cb7c9", label_color=["#6cb7c9", "#344356"],
#                area_opacity=0.7, is_smooth=True, is_toolbox_show=False, is_yaxis_show=False)
#     stream.add("出口流量", stream_time, stream_out, is_fill=True, area_color='#000',
#                area_opacity=0.4, is_smooth=True, is_toolbox_show=False, is_yaxis_show=False,
#                is_legend_show=True, legend_text_color="#6cb7c9", xaxis_line_color="#6cb7c9")
#
#     grid.add(stream, grid_bottom=30, grid_left=30, grid_top=50, grid_right=30)
#     if is_reload:
#         option = grid.get_options()
#         option = TRANSLATOR.translate(option)
#         option = option.as_snippet()
#         return option
#     else:
#         return grid
