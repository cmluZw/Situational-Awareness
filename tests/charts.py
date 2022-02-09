# from pyecharts import Bar,Pie,Line,Radar
#
#行名
# columns=['sql注入','xss攻击','ddos攻击','口令爆破','目录遍历','webshell']
#
# #设置数据
# data1=[208,20,100,809,123,42]
# data2=[10,23,21,94,13,12]
#
# #设置主副标题
# bar=Bar("web应用攻击柱状图","2021年")
# bar.add("linux1",columns,data1,mark_line=["average"], mark_point=["max", "min"])
# bar.add("linux2",columns,data2,mark_line=["average"], mark_point=["max", "min"])
# bar.render()

#饼状图
# pie=Pie('单个ip攻击饼状图','2021年')
# # pie.add("sql注入",columns,data1,center=[25,50],is_legend_show=False)
# pie.add("xss注入",columns,data2,center=[75,50],is_legend_show=False,is_label_show=True)
# pie.render()

# #折线图
# line = Line("web攻击总量发展","2021年")
# #is_label_show是设置上方数据是否显示
# line.add("ddos", columns, data1, is_label_show=True)
# line.add("sql注入", columns, data2, is_label_show=True)
# line.render()


# #雷达图
# radar = Radar("安全水平综合测定", "2021年web")
# #由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
# data1=[[39,10,81,89,13,42]] #传入的是2维数组
# data2=[[90,63,21,94,31,12]]
# #设置最大值
# schema = [
#     ("sql注入", 100), ("ddos",100), ("爆破", 100),
#     ("xss攻击", 100), ("ssh登录", 100), ("目录遍历", 100),
# ]
# #传入坐标
# radar.config(schema)
# radar.add("linux1",data1)
# #一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
# radar.add("windows1",data2,item_color="#1C86EE")
# radar.render()


# from pyecharts import Map,Geo
# from pyecharts import GeoLines, Style
# #将数据处理成列表
#
# locate = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','陕西','甘肃','青海','宁夏','新疆']
#
# GDP_1978 = [108.84,82.65,183.06,87.99,58.04,229.20,81.98,174.80,272.81,249.24,123.72,114.10,66.37,87.00,225.45,162.92,151.00,146.99,185.85,75.85,16.40,67.32,184.61,46.62,69.05,81.07,64.73,15.54,13.00,39.07]
#
# GDP_2017 = [28014.94,18549.19,34016.32,15528.42,16096.21,23409.24,14944.53,15902.68,30632.99,85869.76,51768.26,27018,32182.09,20006.31,72634.15,44552.83,35478.09,33902.96,89705.23,18523.26,4462.54,19424.73,36980.22,13540.83,16376.34,21898.81,7459.9,2624.83,3443.56,10881.96]
#
# list1 = [[locate[i],GDP_1978[i]] for i in range(len(locate))]
#
# list2 = [[locate[i],GDP_2017[i]] for i in range(len(locate))]
#
# map_1 = Map()
#
# map_1.set_global_opts(
#
#     title_opts=opts.TitleOpts(title="2017年全国各省GDP"),
#
#     visualmap_opts=opts.VisualMapOpts(max_=100000)  #最大数据范围
#
#     )
#
# map_1.add("2017年各省GDP", list2, maptype="china")
#
# map_1.add("1978年各省GDP", list1, maptype="china")
#
# map_1.render('map1.html')


# coding:utf-8
from pyecharts import Geo

value = [20, 30, 40, 60, 70, 80, 90, 100, 10]
attr = ['荆州', '长沙', '渭南', '临汾', '十堰', '唐山', '郴州', '铜陵', '呼和浩特']
geo = Geo("全国各地ip来源", width=1200, height=600)
geo.add("攻击ip来源", attr, value, type="effectScatter", border_color="#ffffff", symbol_size=20,is_visualmap=True,visual_range=[0,100],symbol="pin",symbol_color="#FFD700")
geo.render()