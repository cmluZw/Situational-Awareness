import hashlib

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from model.user import User

# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)

#通过输入的用户名查找密码
def selectpassword(username):  #这里返回的密码经由hash加密
    T = User.query.filter_by(username=username).all()
    if T:
        for u in T:
            Tpassword = u.password
        return Tpassword
    else:
        return 0

#密码比对
def check(username,password):
    user = User()
    user.username=username
    Tpassword=selectpassword(username)
    md5password=encode(password)
    if str(md5password) == str(Tpassword):
        return '登录成功'
    else:
        return '登录失败'

#hash编码
def encode(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

def updatepassword(username,password,newpassword):
    user = User()
    user.username=username
    Tpassword=selectpassword(username)
    md5password=encode(password)
    if str(md5password) == str(Tpassword):
        md5newpassword=encode(newpassword)
        result=user.updatepassword(md5newpassword)
        if result:
            return 0 #修改成功
        else:
            return 1 #修改失败
    else:
        return 1 #修改失败

