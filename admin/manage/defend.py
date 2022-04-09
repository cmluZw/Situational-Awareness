import os


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
            return 0
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