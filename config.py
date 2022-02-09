
DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS=True
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456789@127.0.0.1:3306/situational?charset=utf8'


# Web日志路径
apache_log = '/var/log/apache2/access.log'

#爆破次数设定
burst_num=30




#type设置
attackType = {
    0: '无威胁',
    1: 'XSS跨站',
    2: 'SQL注入',
    3: '目录扫描',
    4: 'DoS攻击',
    5: '暴力破解',
    6: '木马后门',
    7: 'SSH爆破'
}