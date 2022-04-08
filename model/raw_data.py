from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)

class Raw_data(db.Model):
    # 声明表名

    __tablename__ = 'raw_data'
    #建立字段
    id = db.Column(db.Integer, primary_key=True)

    srcip = db.Column(db.String(200))

    dstip = db.Column(db.String(200))

    raw_request = db.Column(db.Text())

    time=db.Column(db.String(200))

    def __init__(self, id=None, srcip=None, dstip=None, raw_request=None,time=None):
        self.id = id
        self.srcip = srcip
        self.dstip = dstip
        self.raw_request = raw_request
        self.time=time

    def get_srcip(self):
        return self.srcip

    def get_dstip(self):
        return self.dstip

    def get_time(self):
        return self.raw_request

    def get_raw_request(self):
        return self.raw_request

    def insert(self):
        db.session.add(self)
        db.session.commit()