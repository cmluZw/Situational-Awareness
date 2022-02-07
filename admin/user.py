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
def selectpassword(username):
    T = User.query.filter_by(username=username).all()
    for u in T:
        Tpassword = u.password
    return Tpassword


#密码比对
def check(username,password):
    user = User()
    user.username=username
    Tpassword=selectpassword(username)
    if str(password) == str(Tpassword):
        return '登录成功'
    else:
        return '登录失败'

#hash编码
def encode(self,password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()


# #登录面板
# @app.route('/login',methods=['GET','POST'])
# def check():
#     username = request.form['username']
#     password = request.form['password']
#     user = User()
#     user.username=username
#     Tpassword=selectpassword(username)
#     #print("Tpassword:"+str(Tpassword)+"   password:"+str(password))
#     if str(password) == str(Tpassword):
#         return '登录成功'
#     else:
#         return '登录失败'