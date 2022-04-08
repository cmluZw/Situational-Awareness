from pyecharts import GeoLines, Style

import config
from model.ip import Ip


def selectip():
    ip=Ip()
    ip_attack_list = ip.query.all()
    ip_list=list()
    city_list=list()
    jindu_list=list()
    weidu_list=list()
    country_list=list()
    for i in ip_attack_list:
        ip_list.append(i.ip)
        city_list.append(i.city_name)
        jindu_list.append(i.Location_Latitude)
        weidu_list.append(i.Location_Longitude)
        country_list.append(i.country_name)
    return ip_list,city_list,jindu_list,weidu_list,country_list

style = Style(
    title_color="#fff",
    title_top=20,
    title_pos="center",
    width="auto",
    height="100%",
    background_color="rgba(0,0,0,0)"
)

style_geo = style.add(


    maptype='world',            # 地图类型
    geo_effect_period=4,        # 特效持续时间
    geo_effect_traillength=0.1,  # 特效尾长
    geo_effect_symbol="pin",    # 特效形状
    geo_effect_symbolsize=5,    # 特效尺寸
    is_geo_effect_show=True,    # 是否显示特效
    is_roam=True,               # 鼠标缩放与平移 True, move or scale
    is_label_show=True,         # 是否展示图形上的文本标签
    label_color=['#FFD700', '#FFD700', '#339900'],  # 图形的颜色, 多值循环取值
    label_pos="right",          # 标签位置
    label_text_color="#7BECFF",  # 标签字体颜色
    label_formatter="{b}",      # 标签格式
    line_color="#D3545F",        # 线的颜色
    line_curve=0.2,             # 路径的弧度
    line_opacity=0,             # 线的透明度
    line_width=0,               # 线的宽度
    line_type=None,             # 线的类型
    is_legend_show=False,       # 是否显示图例分类
    is_toolbox_show=False,      # 是否显示工具箱
    border_color="#00FFFF ",     # 国家边界颜色
    geo_normal_color="#1b1f23"  # 国家区域颜色
)

def earthMap():
    # local_city="Beijing"
    local_city=config.local_city
    ip_list, city_list, weidu_list, jindu_list, country_list = selectip()
    # print(ip_list,city_list,weidu_list,jindu_list,country_list)
    world=GeoLines('', **style.init_style)
    districts=list()
    values=list()
    length=len(ip_list)
    for i in range(0,int(length)):
        world.add_coordinate(city_list[i], jindu_list[i],weidu_list[i])#添加自定义经纬度节点
        if city_list[i]== None:
            path=['Beijing',local_city]
            districts.append(path)
        path = [city_list[i], local_city]
        districts.append(path)
    # world.add("",districts, values, maptype='world',is_visualmap=True,is_label_show=False,)
    world.add('', districts, **style_geo)
    print(districts)
    # world.render()
    world.chart_id="earth_map"
    return world
earthMap()
