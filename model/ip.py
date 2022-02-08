from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)

class Ip(db.Model):
    # 声明表名

    __tablename__ = 'attack_ip'

    # 建立字段函数

    id = db.Column(db.Integer, primary_key=True)

    ip = db.Column(db.String(200))

    country_name = db.Column(db.String(200))

    country_specificname = db.Column(db.String(200))

    city_name = db.Column(db.String(200))

    Location_Latitude = db.Column(db.String(200))  #经度

    Location_Longitude = db.Column(db.String(200))  #维度

    time=db.Column(db.String(200))

    #构造方法
    def __init__(self, id=None, ip=None, country_name=None,country_specificname=None,city_name=None,Location_Latitude=None,Location_Longitude=None,time=time):

        self.id = id
        self.ip = ip
        self.country_name=country_name
        self.country_specificname = country_specificname
        self.city_name = city_name
        self.Location_Latitude = Location_Latitude
        self.Location_Longitude = Location_Longitude
        self.time=time

    def getip(self):
        return self.ip

    def getcountry_name(self):
        return self.country_name

    def getcountry_specificname(self):
        return self.country_specificname

    def getcity_name(self):
        return self.city_name

    def getLocation_Latitude(self):
        return self.Location_Latitude

    def getLocation_Longitude(self):
        return self.Location_Longitude

    def gettime(self):
        return self.time

    def insert(self):
        db.session.add(self)
        db.session.commit()

