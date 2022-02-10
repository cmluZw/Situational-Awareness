from pyecharts import Pie,Bar,Line
from model.ssh import Ssh
import admin.ipanalyse as ipanalyse

def selectssh():
    ssh=Ssh()
    ssh_list = ssh.query.all()
    ip_list=list()
    num_list=list()
    for i in ssh_list:
        ip_list.append(i.ip)
        num_list.append(i.num)
    return ip_list,num_list

def sshLineCharts():
    ip_list,num_list=selectssh()
    ssh_line=Line("Ssh爆破攻击趋势图")
    ssh_line.add('Ssh爆破攻击趋势',ip_list,num_list,is_show=True)
    # ssh_line.render()
    return ssh_line
