from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from model.apache import Apache
from model.ip import Ip
from model.network import Network
from model.ssh import Ssh
import admin.ipanalyse as ipanalyse

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

def selectbycountry(country_name):
    ip=Ip()
    list = ip.query.filter_by(country_name=country_name).all()
    return list

def selectbycity(city_name):
    ip=Ip()
    list = ip.query.filter_by(country_specificname=city_name).all()
    if len(list)==0:
        list = ip.query.filter_by(city_name=city_name).all()
    return list


