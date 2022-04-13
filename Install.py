import os
import pymysql
os.popen('pip3 install -r requirements.txt')

sql0='''
create database if not exists situational;
'''

sql1='''
CREATE TABLE `apache` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `num` varchar(255) DEFAULT NULL,
  `attack_type` varchar(255) DEFAULT NULL,
  `raw_request` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
'''
sql2='''
CREATE TABLE `attack_ip` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `country_name` varchar(255) DEFAULT NULL,
  `country_specificname` varchar(255) DEFAULT NULL,
  `city_name` varchar(255) DEFAULT NULL,
  `Location_Latitude` varchar(255) DEFAULT NULL,
  `Location_Longitude` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
'''
sql3='''
CREATE TABLE `danger` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `is_deal` int(11) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
'''
sql4='''
CREATE TABLE `network` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `srcip` varchar(255) DEFAULT NULL,
  `dstip` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `trafficIn` varchar(255) DEFAULT NULL,
  `trafficOut` varchar(255) DEFAULT NULL,
  `attack_type` varchar(255) DEFAULT NULL,
  `raw_request` text,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
'''
sql5='''
CREATE TABLE `raw_data` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `srcip` varchar(255) DEFAULT NULL,
  `dstip` varchar(255) DEFAULT NULL,
  `raw_request` text,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;'''

sql6='''CREATE TABLE `ssh` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `num` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;'''

sql7='''CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;'''

sql8='''insert into user(username,password) values ('admin','e10adc3949ba59abbe56e057f20f883e');'''

def create_db(dbhost,dbusername,dbpassword,dbport):
    db = pymysql.connect(host=dbhost, port=int(dbport), user=dbusername, passwd=dbpassword, charset='utf8')
    cursor = db.cursor()
    try:
        data=cursor.execute(sql0)
    except:
        print('error')


def initialize(dbhost,dbusername,dbpassword,db,dbport):
        # 打开数据库
        db = pymysql.connect(host=dbhost, port=int(dbport), user=dbusername, passwd=dbpassword, db=db, charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        try:
            data = cursor.execute(sql1)
            data = cursor.execute(sql2)
            data = cursor.execute(sql3)
            data = cursor.execute(sql4)
            data = cursor.execute(sql5)
            data = cursor.execute(sql6)
            data = cursor.execute(sql7)
            data = cursor.execute(sql8)
            if (data==0):
                print("数据库创建成功")
            return 1
        except:
            db_exist=cursor.execute("select schema_name from information_schema.schemata where schema_name='situational';")
            if db_exist:
                print('数据库已存在')
            return 2
        else:
            print("数据库错误")
            return 0

if __name__ == "__main__":
    create_db('localhost','root','123456789','3306')
    initialize('localhost','root','123456789','test','3306')