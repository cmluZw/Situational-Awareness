import os

def evilconfig(sqlrule=None,xssrule=None,backrule=None):
    initsqlrule = "'|--|update|extractvalue|union|select|substr|information_schema"
    # XSS 跨站攻击匹配规则
    initxssrule = "script|iframe|javascript|onerror|onmouseover|/>"
    # 木马后门 匹配规则
    initbackrule = "eval|assert|system|shell_exec|passthru"
    if sqlrule!=None:
        sqlrule=initsqlrule+sqlrule
    elif xssrule!=None:
        xssrule=initxssrule+xssrule
    elif backrule!=None:
        backrule=initbackrule+backrule
    else:
        pass
    return sqlrule,xssrule,backrule

def processconfig(processlist):
    process=[]
    if len(processlist)==0:
        process = ['apache', 'mysqld', 'vsftpd', 'sshd']
    else:
        for i in processlist:
            process.append((i))
    return process

def localconfig(ip=None,city=None):
    if ip!=None and city!=None:
        local_ip=ip
        local_city=city
    else:
        local_ip = '10.2.3.2'
        local_city = 'Shanghai'
    return local_ip,local_city

def logconfig(log_path=None):
    if log_path!=None:
        log_path=log_path
    else:
        log_path='/var/log/apache2/access.log'
    return log_path

def emailconfig(server,port,is_use_tls,username,password,recipient):
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '1551505032@qq.com'
    MAIL_PASSWORD = 'zmybnrktcjghfhbe'
    mail_recipient='2534395766@qq.com'
    if server and port and is_use_tls and username and password and recipient:
        MAIL_SERVER=server
        MAIL_PORT=port
        MAIL_USE_TLS=is_use_tls
        MAIL_USERNAME=username
        MAIL_PASSWORD=password
        mail_recipient=recipient
    return MAIL_SERVER,MAIL_PORT,MAIL_USE_TLS,MAIL_USERNAME,MAIL_PASSWORD,mail_recipient