# 导入第三方连接库sql点金术
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 建立对象

app = Flask(__name__)

# 载入配置文件

app.config.from_pyfile('../config.py')

# #指定数据库连接还有库名

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456789@127.0.0.1:3306/test?charset=utf8'


# 指定配置，用来省略提交操作

# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# 建立数据库对象

db = SQLAlchemy(app)


# 建立数据库类，用来映射数据库表,将数据库的模型作为参数传入

class User(db.Model):
    # 声明表名

    __tablename__ = 'user'

    # 建立字段函数

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(200))

    password = db.Column(db.String(200))


# 数据库的查询操作（查）

@app.route("/select")
def select_user():
    # 简单的全量查询

    # 翻译为 select * from user

    ulist = User.query.all()

    print(ulist)

    for item in ulist:
        print(item.username)

    # 只取一条

    # 翻译为 select * from user limit 1

    ulist = User.query.first()

    print(ulist)

    # 使用原生的sql语句

    # 翻译为 select * from user order by id desc limit 1,2

    items = db.session.execute(' select * from user order by id desc ')

    # 将结果集强转为list

    items = list(items)

    # 使用原生语句进行修改操作

    # db.session.execute(" update user set password = '321321' where id = 6 ")

    # 将动态数据传递给模板

    return 'select'
# 数据库的修改操作（改）

@app.route("/edit")
def edit_user():
    # 根据某个字段做修改操作

    # 翻译为 update user set name = '张三' where id = 2

    User.query.filter_by(id=3).update({'username': '张三'})

    return '这里是修改操作'


# 数据库的删除操作（删）

@app.route("/del")
def del_user():
    # 根据某个字段做删除,filter_by可以理解为where条件限定

    # 翻译为 delete from user where id = 1

    User.query.filter_by(id=1).delete()

    return '这里是删除操作'


# 数据库的入库操作（增）

@app.route("/")
def index():
    # 增，入库逻辑

    # 声明对象

    user = User(username='你好你好', password='456456')

    # 调用添加方法

    db.session.add(user)

    # 提交入库

    # db.session.commit()

    return '这里是首页'#导入第三方连接库sql点金术
