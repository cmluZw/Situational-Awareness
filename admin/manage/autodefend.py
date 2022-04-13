import time
from charts.manage import dangerous_manageCharts
from charts.manage.dangerous_manageCharts import dealdanger

while 1:
    dealdanger()
    time.sleep(7200)#每两个小时执行一次