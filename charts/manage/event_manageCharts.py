from admin.manage import event_manage
from pyecharts import Pie

def dealevent_numCharts(ip):
    event_num=event_manage.selectevent_byip(ip)
    return event_num

# dealevent_numCharts("101.33.228.166")

