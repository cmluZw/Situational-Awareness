from pyecharts_javascripthon.api import TRANSLATOR

from admin.processanalyse import processStatus
from pyecharts import EffectScatter, Grid

def processCharts():  #散点图，坐标系
    symbol_size = 5
    processstatus=processStatus()#{'apache': 0, 'mysqld': 0, 'vsftpd': 0, 'sshd': 1}
    # print(processstatus)
    grid = Grid(width="100%", height="100%")

    effectscatter = EffectScatter()
    x=[10]
    down = "#F52E44"  # 红灯宕机
    up = "#01A901"  # 绿灯正常
    colors = [down] * 4
    if processstatus['apache']:
        colors[0] = up
    if processstatus['mysqld']:
        colors[1] = up
    if processstatus['sshd']:
        colors[2] = up
    if processstatus['vsftpd']:
        colors[3] = up
    # print(colors)
    effectscatter.add("apache", x, [1], symbol_size=symbol_size, effect_scale=3.5,
                effect_period=2, label_color=colors)
    effectscatter.add("mysql", x, [2], symbol_size=symbol_size, effect_scale=3.5,
                effect_period=2, label_color=colors)
    effectscatter.add("ssh", x, [3], symbol_size=symbol_size, effect_scale=3.5,
                effect_period=2, label_color=colors)
    effectscatter.add("ftp", x, [4], symbol_size=symbol_size, effect_scale=3.5,
                effect_period=2, label_color=colors, is_toolbox_show=False,
                is_label_show=False, is_xaxis_show=False, is_yaxis_show=False, is_legend_show=False)
    # effectscatter.render()

    grid.add(effectscatter,grid_right=30, grid_top=10, grid_bottom=5)
    # grid.render()
    return grid



# processCharts()  #测试成功