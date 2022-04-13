from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)


class Ssh(db.Model):
    # 声明表名

    __tablename__ = 'ssh'

    # 建立字段函数

    id = db.Column(db.Integer, primary_key=True)

    ip = db.Column(db.String(200))

    time = db.Column(db.String(200))

    num = db.Column(db.String(200))

    #构造方法
    def __init__(self, id=None, ip=None, time=None,num=None):

        self.id = id
        self.ip = ip
        self.time=time
        self.num=num

    def getip(self):
        return self.ip

    def gettime(self):
        return self.time

    def getnum(self):
        return self.num

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def selectevent_byip(self):
        sql = "SELECT num from ssh where ip='{}'".format(self.ip)
        data = db.session.execute(sql)
        data_list = data.fetchall()
        # print(data.fetchall())
        return data_list
