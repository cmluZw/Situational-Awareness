from pyecharts import Bar,Pie,Line,Radar,Geo,GeoLines, Style
from flask import Flask,render_template,request


def barchart():
    # 行名
    columns=['sql注入','xss攻击','ddos攻击','口令爆破','目录遍历','webshell']

    #设置数据
    data1=[208,20,100,809,123,42]
    data2=[10,23,21,94,13,12]

    #设置主副标题
    bar=Bar()
    bar.add("linux1",columns,data1,mark_line=["average"], mark_point=["max", "min"])
    bar.add("linux2",columns,data2,mark_line=["average"], mark_point=["max", "min"])
    bar.chart_id="bar"
    return bar

def piechart():
    columns = ['sql注入', 'xss攻击', 'ddos攻击', '口令爆破', '目录遍历', 'webshell']

    # 设置数据
    data1 = [208, 20, 100, 809, 123, 42]
    data2 = [10, 23, 21, 94, 13, 12]
    # 饼状图
    pie=Pie()
    # pie.add("sql注入",columns,data1,center=[25,50],is_legend_show=False)
    pie.add("xss注入",columns,data2,center=[75,50],is_legend_show=False,is_label_show=True)
    pie.chart_id="pie"
    pie.render()
    return pie

def linechart():
    #折线图
    columns = ['sql注入', 'xss攻击', 'ddos攻击', '口令爆破', '目录遍历', 'webshell']

    # 设置数据
    data1 = [208, 20, 100, 809, 123, 42]
    data2 = [10, 23, 21, 94, 13, 12]
    line = Line()
    #is_label_show是设置上方数据是否显示
    line.add("ddos", columns, data1, is_label_show=True)
    line.add("sql注入", columns, data2, is_label_show=True)
    line.chart_id="line"
    line.render()
    return line


def radarchart():
    #雷达图
    radar = Radar()
    #由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
    data1=[[39,10,81,89,13,42]] #传入的是2维数组
    data2=[[90,63,21,94,31,12]]
    #设置最大值
    schema = [
        ("sql注入", 100), ("ddos",100), ("爆破", 100),
        ("xss攻击", 100), ("ssh登录", 100), ("目录遍历", 100),
    ]
    #传入坐标
    radar.config(schema)
    radar.add("linux1",data1)
    #一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
    radar.add("windows1",data2,item_color="#1C86EE")
    radar.chart_id="radar"
    radar.render()
    return radar

# def earthchart():
#     value = [20, 30, 40, 60, 70, 80, 90, 100, 10]
#     attr = ['荆州', '长沙', '渭南', '临汾', '十堰', '唐山', '郴州', '铜陵', '呼和浩特']
#     geo = Geo("全国各地ip来源", width=1200, height=600)
#     geo.add("攻击ip来源", attr, value, type="effectScatter", border_color="#ffffff", symbol_size=20,is_visualmap=True,visual_range=[0,100],symbol="pin",symbol_color="#FFD700")
#     geo.chart_id="geo"
#     geo.render()

def earthchart():
    style = Style(
        title_color="#fff",
        title_top=20,
        title_pos="center",
        width="auto",
        height="100%",
        background_color="rgba(0,0,0,0)"
    )

    style_geo = style.add(

        maptype='world',  # 地图类型
        # geo_effect_period=4,        # 特效持续时间
        # geo_effect_traillength=0.1,  # 特效尾长
        # geo_effect_symbol="pin",    # 特效形状
        # geo_effect_symbolsize=5,    # 特效尺寸
        # is_geo_effect_show=True,    # 是否显示特效
        # is_roam=True,               # 鼠标缩放与平移 True, move or scale
        # is_label_show=True,         # 是否展示图形上的文本标签
        # label_color=['#339900', '#339900', '#339900'],  # 图形的颜色, 多值循环取值
        # label_pos="right",          # 标签位置
        # label_text_color="#7BECFF",  # 标签字体颜色
        # label_formatter="{b}",      # 标签格式
        # # line_color="#D3545F",        # 线的颜色
        # line_curve=0.2,             # 路径的弧度
        # line_opacity=0,             # 线的透明度
        # line_width=0,               # 线的宽度
        # line_type=None,             # 线的类型
        # is_legend_show=False,       # 是否显示图例分类
        # is_toolbox_show=False,      # 是否显示工具箱
        # border_color="#6cb7c9",     # 国家边界颜色
        # geo_normal_color="rgba(12,12,12,0.5)"  # 国家区域颜色
        is_legend_show=False,  # 是否显示图例分类
        is_toolbox_show=False,  # 是否显示工具箱
        is_geo_effect_show=True,  # 是否显示特效
        is_roam=True,  # 鼠标缩放与平移 True, move or scale
        line_curve=0.3,  # 轨迹线的弯曲度，0-1
        line_opacity=0.6,  # 轨迹线的透明度，0-1
        geo_effect_symbol='plane',  # 特效的图形，有circle,plane,pin等等
        geo_effect_symbolsize=10,  # 特效图形的大小
        geo_effect_color='#DB6A50',  # 特效的颜色
        geo_effect_traillength=0.1,  # 特效图形的拖尾效果，0-1
        label_color=['#FFA421', '#D3545F'],  # 轨迹线的颜色，标签点的颜色，
        border_color='#6cb7c9',  # 边界的颜色
        geo_normal_color='#478A84',  # 地图的颜色
    )

    local_city = "Chengdu"
    ip_list=['101.33.228.162', '101.35.190.224', '101.42.235.153', '101.43.143.195', '101.43.67.184', '101.43.82.79',
     '101.43.96.248', '109.130.122.122', '109.234.28.177', '116.206.13.164', '1.180.72.24', '1.180.72.27',
     '159.65.133.99', '174.57.125.77', '175.24.172.9', '211.36.138.57', '222.67.18.158', '223.113.52.38',
     '24.8.141.118', '31.184.198.71', '39.109.246.117', '58.34.189.28', '79.41.252.45', '86.236.215.173',
     '93.148.57.144']
    city_list=[
        'None', 'None', 'None', 'None', 'None', 'None', 'None', 'Brussels', 'Kochubeyevskoye', 'Bandung', 'Ordos', 'Ordos', 'Singapore', 'Secaucus', 'None', 'Gwanak-gu', 'Shanghai', 'None', 'Denver', 'St Petersburg', 'Singapore', 'Shanghai', 'Verona', 'Saint-Doulchard', 'Milan']
    weidu_list=[
        '39.9289', '39.9289', '39.9289', '39.9289', '39.9289', '39.9289', '39.9289', '50.8451', '44.6897', '-6.9216999999999995', '39.6', '39.6', '1.2929', '40.7876', '34.7725', '37.4687', '31.0449', '34.7725', '39.6814', '59.8981', '1.2929', '31.0449', '45.4299', '47.1037', '45.4707']
    jindu_list=[
        '116.3883', '116.3883', '116.3883', '116.3883', '116.3883', '116.3883', '116.3883', '4.3557', '41.8267', '107.6071', '109.7833', '109.7833', '103.8547', '-74.06', '113.7266', '126.9458', '121.4012', '113.7266', '-104.8837', '30.2619', '103.8547', '121.4012', '10.9844', '2.352', '9.1889']
    country_list=[
        'China', 'China', 'China', 'China', 'China', 'China', 'China', 'Belgium', 'Russia', 'Indonesia', 'China', 'China', 'Singapore', 'United States', 'China', 'South Korea', 'China', 'China', 'United States', 'Russia', 'Singapore', 'China', 'Italy', 'France', 'Italy']
    world = GeoLines("全球攻击情况统计", "", title_pos='center', width=1000, height=1000)
    districts = list()
    values = list()
    length = len(ip_list)
    for i in range(0, int(length)):
        world.add_coordinate(city_list[i], jindu_list[i], weidu_list[i])  # 添加自定义经纬度节点
        if city_list[i] == None:
            path = ['Beijing', local_city]
            districts.append(path)
        path = [city_list[i], local_city]
        districts.append(path)
    # world.add("",districts, values, maptype='world',is_visualmap=True,is_label_show=False,)
    world.add('', districts, **style_geo)
    print(districts)
    # world.render()
    world.chart_id = "earth_map"
    return world
# earthchart()

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    Piechart=piechart()
    Barchart=barchart()
    Earthchart=earthchart()
    Radarchart=radarchart()
    Linechart=linechart()
    return render_template('base.html',
                           Piechart=Piechart.render_embed(),
                           Piechart_id=Piechart.chart_id,
                           Barchart=Barchart.render_embed(),
                           Barchart_id=Barchart.chart_id,
                           Earthchart=Earthchart.render_embed(),
                           Earthchart_id=Earthchart.chart_id,
                           Radarchart=Radarchart.render_embed(),
                           Radarchart_id=Radarchart.chart_id,
                           Linechart=Linechart.render_embed(),
                           Linechart_id=Linechart.chart_id,
                           )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)