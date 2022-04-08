from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)


class Danger(db.Model):
    # 声明表名

    __tablename__ = 'danger'

    # 建立字段函数

    id = db.Column(db.Integer, primary_key=True)

    ip = db.Column(db.String(200))

    time = db.Column(db.String(200))

    is_deal = db.Column(db.Integer)

    #构造方法
    def __init__(self, id=None, ip=None, time=None,is_deal=0):

        self.id = id
        self.ip = ip
        self.time=time
        self.is_deal=is_deal

    def getip(self):
        return self.ip

    def gettime(self):
        return self.time

    def getis_deal(self):
        return self.is_deal

    def insert(self):
        db.session.add(self)
        db.session.commit()
