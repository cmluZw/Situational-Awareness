# -*- coding:utf-8 -*-
# Author : woodsay
# Date   : 2019/5/5
# File   : MultiLinkDetect.py
# For    : 对同一IP多次连接请求的探测
from os import popen
from json import dumps
import config
from model.apache import Apache

#默认路径为apache_log = '/var/log/apache2/access.log'
#默认爆破次数为5，burst_num=5
def apacheanalyse():


    cmd = "cat %s | awk -F' ' '{print $1}' | uniq -c | sort -n " % config.apache_log
    count_cmd = cmd + "| awk -F' ' '{print $1}' "
    ip_cmd = cmd + "| awk -F' ' '{print $2}' "

    count_result = popen(count_cmd)
    ip_result = popen(ip_cmd)

    counts = count_result.read().split()
    ips = ip_result.read().split()

    ip_result.close()
    count_result.close()

    ##以上将统计数量和ip结果赋值成功

# 分析爆破,如果请求的是同一个文件记为爆破，请求次数设为30

    length=len(ips)
    for i in range(0,length):
        count=counts[i]
        if int(count)>int(config.burst_num):  #记为爆破
            addr=ips[i]
            cmd = "cat {} | grep {} | ".format(config.apache_log, addr)
            file_cmd = cmd + "awk '{print $7}'"  #请求数据
            time_cmd = cmd + "awk '{print $4}'" #时间
            time_result = popen(time_cmd)
            file_result = popen(file_cmd)
            # 取最后50次访问的时间，判断是否是短时间内连续访问
            times = time_result.read().split()[-30:]
            # 取最后50次访问的文件，判断是否是短时间内请求同一文件
            files = file_result.read().split()[-30:]
            time_result.close()
            file_result.close()
            # Apache日志的标准时间格式为: 08/Apr/2019:17:35:07
            stime_h = int(times[0][-8:-6])
            stime_m = int(times[0][-5:-3])
            etime_h = int(times[-1][-8:-6])
            etime_m = int(times[-1][-5:-3])
            if etime_h == stime_h and etime_m - stime_m < 2: #在两分钟内请求超过一定次数
                apache=Apache()
                apache.ip=addr
                apache.num=count
                apache.time=times[0]
                # 如果是请求的都是同一文件则判断为暴力破解,类型为5
                if files[-1] == files[-2] == files[-3] == files[-4]:
                    apache.raw_request = files[-1]
                    apache.attack_type=5
                # 否则判断为目录扫描
                else:
                    apache.attack_type = 3
                apache.insert()  #存入数据库
                #print(apache.getip(),apache.getnum(),apache.getattack_type(),apache.getraw_request()) 测试成功
            else:
                pass
