import os
import re
import config

def defend(ip):
#     禁ip命令:
#     '''iptables -A INPUT -p tcp -s 182.150.63.121 -j DROP
# iptables -A INPUT -p tcp -s 182.150.63.121 -j ACCEPT
# if iptables -A INPUT -p tcp -s 182.150.63.121 -j ACCEPT;then echo 1;fi '''
    try:
        cmd="if iptables -A INPUT -p tcp -s {} -j DROP;then echo 1;fi".format(ip)
        stream = os.popen(cmd)
        # 获取执行结果
        output = stream.read().split()
        stream.close()
        if output:
            return 0#防御成功
        return 1
    except:
        return 1

def accept(ip):
    try:
        cmd="if iptables -A INPUT -p tcp -s {} -j ACCEPT;then echo 1;fi".format(ip)
        stream = os.popen(cmd)
        # 获取执行结果
        output = stream.read().split()
        stream.close()
        if output:
            return 0
        return 1
    except:
        return 1

def lockfile(path):
    # 锁死文件夹
    # '''chattr -R +i /var/www/html'''
    # 解锁文件夹
    # ''' chattr -R -i /var/www/html'''
    try:
        cmd="if chattr -R +i {path};then echo 1;fi".format(path)
        stream = os.popen(cmd)
        # 获取执行结果
        output = stream.read().split()
        stream.close()
        if output:
            return 0
        return 1
    except:
        return 1
def unlockfile(path):
    try:
        cmd="if chattr -R -i {path};then echo 1;fi".format(path)
        stream = os.popen(cmd)
        # 获取执行结果
        output = stream.read().split()
        stream.close()
        if output:
            return 0
        return 1
    except:
        return 1


def waffilter(x): #为了本系统的安全性，设置waf
    sqlrule = config.sqlrule
    xssrule=config.xssrule
    backrule=config.backrule
    rule=sqlrule+xssrule+backrule
    for i in rule:
        if i in x:
            x=x.split(i)[0]
            print(x)
        else:
            pass
    return x