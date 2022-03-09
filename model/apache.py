from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)


class Apache(db.Model):
    # 声明表名

    __tablename__ = 'apache'

    # 建立字段函数

    id = db.Column(db.Integer, primary_key=True)

    ip = db.Column(db.String(200))

    time = db.Column(db.String(200))

    num = db.Column(db.String(200))

    attack_type=db.Column(db.String(200))

    raw_request=db.Column(db.String(20000))

    #构造方法
    def __init__(self, id=None, ip=None, time=None,num=None,attack_type=None,raw_request=None):

        self.id = id
        self.ip = ip
        self.time=time
        self.num=num
        self.attack_type=attack_type
        self.raw_request=raw_request

    def getip(self):
        return self.ip

    def gettime(self):
        return self.time

    def getnum(self):
        return self.num

    def getattack_type(self):
        return self.attack_type

    def getraw_request(self):
        return self.raw_request

    def insert(self):
        db.session.add(self)
        db.session.commit()