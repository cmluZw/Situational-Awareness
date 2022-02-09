
DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS=True
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456789@127.0.0.1:3306/situational?charset=utf8'


# Web日志路径
apache_log = '/var/log/apache2/access.log'

#爆破次数设定
burst_num=30

# SQL 注入攻击匹配规则
sqlrule = "'|--|update|extractvalue|union|select|substr|information_schema".split(
    '|')
# XSS 跨站攻击匹配规则
xssrule = "script|iframe|javascript|onerror|onmouseover|/>".split('|')
# 木马后门 匹配规则
backrule = "eval|assert|system|shell_exec|passthru".split('|')


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