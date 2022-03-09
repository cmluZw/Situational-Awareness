from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from model.ssh import Ssh
import admin.ipanalyse as ipanalyse
import os


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)


#通过统计命令写入文件便于后续分析，这里的latsb是登录失败的日志
def logBycmd():
    ssh_fp = open('./output/analyse/ssh_analyse.txt', 'w')

    cmd = "lastb | grep ssh |awk '{print $3}' | sort | uniq -c"  # 统计了次数和ip
    stream = os.popen(cmd)
    # 获取执行结果
    output = stream.read().split()
    stream.close()
    for i in output:
        print(i)
        ssh_fp.write(i+'\n')
    ssh_fp.close()
'''
num
ip
num
ip
'''


# 将ssh的信息存入表，注意，这里是两个表，一个ssh表，ssh表中存放的是ip和num，一个ip表，ip表中存放的是关于ip的经纬度等等
def analyseByfile():
    # logBycmd()
    #执行命令，将执行结果写入文件ssh_analyse
    '''监控 ssh 的失败登录日志'''
    ssh_fp = open('output/analyse/ssh_analyse.txt', 'r')
    raw_data = ssh_fp.readlines()
    ssh_fp.close()
    length=len(raw_data)-2 #这里-2是为了除去最后的日期 sat 22
    half=int(length/2)
    if length%2!=0:
        return '日志错误'
    num=list()
    ip=list()
    for i in range(0,length):
        if i%2==0:
            num.append(raw_data[i])
        else:
            ip.append(raw_data[i])
    for j in range(0,half):
        ssh=Ssh()
        ssh.num=num[j]
        ssh.ip=ip[j]
        ssh.insert()
        ipanalyse.seperate_ip(ssh.ip.split('\n')[0])


# analyseByfile()