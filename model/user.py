import hashlib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)

class User(db.Model):
    # 声明表名

    __tablename__ = 'user'

    # 建立字段函数

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(200))

    password = db.Column(db.String(200))



    #构造方法
    def __init__(self, id=None, username=None, password=None,):

        self.id = id
        self.username = username
        self.password=password

    def getusername(self):
        return self.username

    def getpassword(self):
        return self.password

    def updatepassword(self,newpassword):
        sql = "update user set password='{0}' where username='{1}'".format(newpassword,self.username)
        data = db.session.execute(sql)
        return data

