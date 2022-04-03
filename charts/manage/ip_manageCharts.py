import json
from pyecharts import Pie,Map
import admin.manage.ip_manage as ip_manage

def selectby_countryCharts():
    country_name_list,num_list=ip_manage.Statisticsip()
    ipcountry_pie = Pie()
    ipcountry_pie.add("ip来源国家统计", country_name_list, num_list, radius=[28, 38], label_text_color=None,
                legend_orient='vertical', center=[15, 25], is_legend_show=False, is_toolbox_show=False,
                is_label_show=False,
                label_color=['#8080C0', '#007979', '#97CBFF', '#2894FF', '#E8FFC4', '#CDCD9A', '#C4E1E1', '#4A4AFF',
                             '#2894FF', '#AAAAFF', '#4DFFFF', '#9D9D9D'])
    return ipcountry_pie

# selectby_countryCharts()

def selectalllistCharts():
    all_list=ip_manage.selectall()
    length=len(all_list)
    ip_list,country_name,country_specificname,city_name,time=[],[],[],[],[]
    # return all_list,length
    for i in all_list:
        ip_list.append(i.ip)
        country_name.append(i.country_name)
        country_specificname.append(i.country_specificname)
        city_name.append(i.city_name)
        time.append(i.time)
    return length,ip_list,country_name,country_specificname,city_name,time
    #     print(i.ip)
    #     print(i.country_name)
    #     print(i.country_specificname)
    #     print(i.city_name)
    #     print(i.time)

# selectalllistCharts()

#查询功能完成
def ip_searchCharts(x):
    list=ip_manage.ip_search(x)
    length = len(list)
    ip_list, country_name, country_specificname, city_name, time = [], [], [], [], []
    # return all_list,length
    for i in list:
        ip_list.append(i.ip)
        country_name.append(i.country_name)
        country_specificname.append(i.country_specificname)
        city_name.append(i.city_name)
        time.append(i.time)
    # print(length, ip_list, country_name, country_specificname, city_name, time)
    return length, ip_list, country_name, country_specificname, city_name, time
