import psutil
import config


def processStatus():
    process_status = {}
    process = config.process
    for i in process:
        process_status[i]=0
    process_all=set()
    process_run=psutil.process_iter()#获取正在运行的进程，返回进程对象列表
    for i in process_run:
        try:
            process_all.add(i)
        except:
            pass
    for i in process_all:
        try:
            for p in process:
                if p.lower() in i.name().lower():
                    process_status[p]=1
        except:
            pass
    return process_status
    # print(process_status)
    #测试成功
    #{'apache': 0, 'mysqld': 0, 'vsftpd': 0, 'sshd': 1}
