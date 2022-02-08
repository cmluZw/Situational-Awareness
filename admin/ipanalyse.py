
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import re
import geoip2.database
from model.ip import Ip
import time


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('../config.py')
# 创建数据库对象
db = SQLAlchemy(app)


reader = geoip2.database.Reader(r'D:\bishe\Situational-Awareness\libs\GeoLite2-City.mmdb')


# 查询IP地址对应的物理地址
def ip_get_location(ip_address):
    # 载入指定IP相关数据
    response = reader.city(ip_address)

    # 读取国家代码
    Country_IsoCode = response.country.iso_code
    # 读取国家名称
    Country_Name = response.country.name
    # 读取国家名称(中文显示)
    Country_NameCN = response.country.names['zh-CN']
    # 读取州(国外)/省(国内)名称
    Country_SpecificName = response.subdivisions.most_specific.name
    # 读取州(国外)/省(国内)代码
    Country_SpecificIsoCode = response.subdivisions.most_specific.iso_code
    # 读取城市名称
    City_Name = response.city.name
    # 读取邮政编码
    City_PostalCode = response.postal.code
    # 获取纬度
    Location_Latitude = response.location.latitude
    # 获取经度
    Location_Longitude = response.location.longitude

    if (Country_IsoCode == None):
        Country_IsoCode = "None"
    if (Country_Name == None):
        Country_Name = "None"
    if (Country_NameCN == None):
        Country_NameCN = "None"
    if (Country_SpecificName == None):
        Country_SpecificName = "None"
    if (Country_SpecificIsoCode == None):
        Country_SpecificIsoCode = "None"
    if (City_Name == None):
        City_Name = "None"
    if (City_PostalCode == None):
        City_PostalCode = "None"
    if (Location_Latitude == None):
        Location_Latitude = "None"
    if (Location_Longitude == None):
        Location_Longitude = "None"

    Time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # print('================Start===================')
    # print('[*] Target: ' + ip_address + ' GeoLite2-Located ')
    # print(u'  [+] 国家编码:        ' + Country_IsoCode)
    # print(u'  [+] 国家名称:        ' + Country_Name)
    # print(u'  [+] 国家中文名称:    ' + Country_NameCN)
    # print(u'  [+] 省份或州名称:    ' + Country_SpecificName)
    # print(u'  [+] 省份或州编码:    ' + Country_SpecificIsoCode)
    # print(u'  [+] 城市名称 :       ' + City_Name)
    # print(u'  [+] 城市邮编 :       ' + City_PostalCode)
    # print(u'  [+] 纬度:            ' + str(Location_Latitude))
    # print(u'  [+] 经度 :           ' + str(Location_Longitude))
    # print('===============End======================')

    ip=Ip()
    ip.ip=ip_address
    ip.city_name=City_Name
    ip.country_name=Country_Name
    ip.country_specificname=Country_SpecificName
    ip.Location_Latitude=Location_Latitude
    ip.Location_Longitude=Location_Longitude
    ip.time=Time
    ip.insert()
# 检验和处理ip地址
def seperate_ip(ip_address):
    ip_match = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)\.)(?:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(?:25[0-4]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)$"
    ip_match_list = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)\.)(?:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(?:25[0-4]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9])-(?:25[0-4]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)$"

    if re.match(ip_match, ip_address):
        try:
            ip_get_location(ip_address)
        except Exception as e:
            print(e)
    elif re.match(ip_match_list, ip_address):
        ip_start = ip_address.split('-')[0].split('.')[3]
        ip_end = ip_address.split('-')[1]
        # 如果ip地址范围一样，则直接执行
        if (ip_start == ip_end):
            try:
                seperate_ip(ip_address.split('-')[0])
            except Exception as e:
                print(e)
        elif ip_start > ip_end:
            print('the value of ip, that you input, has been wrong! try again!')
            exit(0)
        else:
            ip_num_list = ip_address.split('-')[0].split('.')
            ip_num_list.pop()
            for ip_last in range(int(ip_start), int(ip_end) + 1):
                ip_add = '.'.join(ip_num_list) + '.' + str(ip_last)
                try:
                    ip_get_location(ip_add)
                except Exception as e:
                    print(e)
    else:
        print('Wrong type of ip address!')
        print('100.8.11.58  100.8.11.58-100  alike!')


# if __name__ == '__main__':
#     seperate_ip('182.150.63.124')
