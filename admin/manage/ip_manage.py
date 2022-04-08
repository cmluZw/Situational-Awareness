from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from model.apache import Apache
from model.ip import Ip
from model.network import Network
from model.ssh import Ssh
import admin.ipanalyse as ipanalyse
import re


'''写ip管理'''

#从数据库中查询出ip
def selectip_bydb():
    apache = Apache()
    ssh=Ssh()
    network=Network()
    apache_list=Apache.query.all()
    Network_list=Network.query.all()
    Ssh_list = Ssh.query.all()
    ip_list,network_ip_list,network_attack_type_list,num_list,attack_type_list=[],[],[],[],[]
    for i in apache_list:
        ip_list.append(i.ip)
        num_list.append(i.num)
        attack_type_list.append(i.attack_type)
    for i in Ssh_list:
        ip_list.append(i.ip)
        num_list.append(i.num)
        attack_type_list.append("107")
    for i in Network_list:
        network_ip_list.append(i.srcip)
        network_attack_type_list.append(i.attack_type)
    return ip_list,network_ip_list,network_attack_type_list,num_list,attack_type_list


def ip_analyse():
    ip_list,network_ip_list,network_attack_type_list,num_list,attack_type_list=selectip_bydb()
    for i in ip_list:
        ipanalyse.seperate_ip(i.split('\n')[0])
    for i in network_ip_list:
        ipanalyse.seperate_ip(i.split('\n')[0])


def ip_search(x):
    ip = Ip()
    is_ip=re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', x)
    if is_ip:
        list = ip.query.filter_by(ip=x).all()
    else:
        list = ip.query.filter_by(country_name=x).all()
        if len(list)==0:
            list = ip.query.filter_by(country_specificname=x).all()
            if len(list) == 0:
                list = ip.query.filter_by(city_name=x).all()
    return list

# ip_search("1.180.72.24")


def selectbycountry(country_name):
    ip=Ip()
    list = ip.query.filter_by(country_name=country_name).all()
    return list

def selectbyip(ip):
    ip=Ip()
    list = ip.query.filter_by(ip=ip).all()
    return list

def selectbycity(city_name):
    ip=Ip()
    list = ip.query.filter_by(country_specificname=city_name).all()
    if len(list)==0:
        list = ip.query.filter_by(city_name=city_name).all()
    return list

def Statisticsip():
    ip = Ip()
    list=ip.Statisticsip()
    country_name_list,num_list=[],[]
    for i in list:
        country_name_list.append(i.country_name)
        num_list.append(i.num)
    return country_name_list,num_list


def StatisticsipChina():
    ip = Ip()
    list=ip.StatisticsipChina()
    country_name_list,num_list=[],[]
    for i in list:
        country_name_list.append(i.city_name)
        num_list.append(i.num)
    return country_name_list,num_list

def selectall():
    ip = Ip()
    all_list=ip.query.all()
    return all_list
