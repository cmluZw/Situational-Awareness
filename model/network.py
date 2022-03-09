from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)

class Network(db.Model):
    # 声明表名

    __tablename__ = 'network'
    #建立字段
    id = db.Column(db.Integer, primary_key=True)

    srcip = db.Column(db.String(200))

    dstip = db.Column(db.String(200))

    time = db.Column(db.String(200))

    attack_type=db.Column(db.String(200))

    raw_request=db.Column(db.String(20000))

    all_time = {'00:00': [0, 0], '01:00': [0, 0], '02:00': [0, 0], '03:00': [0, 0], '04:00': [0, 0], '05:00': [0, 0],
                '06:00': [0, 0], '07:00': [0, 0], '08:00': [0, 0], '09:00': [0, 0], '10:00': [0, 0], '11:00': [0, 0],
                '12:00': [0, 0], '13:00': [0, 0], '14:00': [0, 0], '15:00': [0, 0], '16:00': [0, 0], '17:00': [0, 0],
                '18:00': [0, 0], '19:00': [0, 0], '20:00': [0, 0], '21:00': [0, 0], '22:00': [0, 0], '23:00': [0, 0],
                }
    # 辅助变量
    tmp_time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00',
                '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00',
                '22:00', '23:00']

    # 入口流量
    trafficIn = 0

    # 出口流量
    trafficOut = 0

    def __init__(self,id=None,srcip=None,dstip=None,time=None,num=None,attack_type=None,raw_request=None,trafficIn=0,trafficOut=0):
        self.id=id
        self.srcip=srcip
        self.dstip=dstip
        self.time=time
        self.attack_type=time
        self.raw_request=raw_request
        self.trafficIn=trafficIn
        self.trafficOut=trafficOut

    def get_srcip(self):
        return self.srcip

    def get_dstip(self):
        return self.dstip

    def get_time(self):
        return self.time

    def get_attack_type(self):
        return self.attack_type

    def get_raw_request(self):
        return self.raw_request

    def get_trafficIn(self):
        return self.trafficIn

    def get_trafficOut(self):
        return self.trafficOut

    def insert(self):
        db.session.add(self)
        db.session.commit()