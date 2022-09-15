# 本系统开源，最新版请访问https://github.com/cmluZw/Situational-Awareness/，拒绝一切形式的非本人授权的商业行为！
# by:CmluZw
# -*- coding:utf-8 -*-
from threading import Thread

from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from admin import user, ipanalyse, sshanalyse, networkanalyse, processanalyse, apacheanalyse
from charts import apacheCharts, earthMapCharts, sshCharts, networkCharts, processCharts, attackeventCharts
from charts.manage import ip_manageCharts, dangerous_manageCharts, event_manageCharts
from admin.manage import ip_manage, event_manage
from flask_mail import Mail, Message
from admin.manage import dangerous_manage
from admin.manage import defend as Defend

# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('config.py')
# 创建数据库对象
db = SQLAlchemy(app)
# #面板首页
# @app.route('/',methods=['GET','POST'])
# def index():
#     return 'Hello World!'


ncap = Thread(target=networkanalyse.networkanalyse)
ncap.start()

check = Thread(target=dangerous_manage.danger)
check.start()


# 初始化
@app.route('/', methods=['GET', 'POST'])
def init():
    if session.get('username') != 'admin':
        return render_template('login.html')
    else:
        # sshanalyse.analyseByfile()
        # apacheanalyse.apacheanalyse()
        return redirect(url_for('index'))


# 登录面板
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        username = Defend.waffilter(username)  # 过滤处理
        password = Defend.waffilter(password)

        info = user.check(str(username), str(password))
        if info == '登录成功':
            session['username'] = 'admin'
            return redirect(url_for('index'))
        else:
            return render_template('login.html', login_info='账号或密码错误')
    else:
        return render_template('login.html')


# 密码修改
@app.route('/admin_info', methods=['GET', 'POST'])
def admin_info():
    if session.get('username') != 'admin':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        newpassword = request.form['newpassword']
        renewpassword = request.form['renewpassword']

        username = Defend.waffilter(username)  # 过滤处理
        password = Defend.waffilter(password)
        newpassword = Defend.waffilter(newpassword)
        renewpassword = Defend.waffilter(renewpassword)

        if newpassword != renewpassword:
            info = "两次密码错误"
            return render_template('manage/admin_info.html', info=info)
        info = user.updatepassword(str(username), str(password), str(newpassword))
        if info:  # 修改失败
            info = "密码错误"
            return render_template('manage/admin_info.html', info=info, )
        else:
            info = "修改成功"
            return render_template('manage/admin_info.html', info=info)
    else:
        return render_template('manage/admin_info.html')


# #防火墙
# @app.route('/defend',methods=['GET','POST'])
# def defend():
#     ip = request.form['defend_ip']
#     dangerous_manageCharts.dealdangerbyself(ip)


# ip管理
@app.route('/ip_manage', methods=['GET', 'POST'])
def ip_manage():
    if session.get('username') != 'admin':
        return render_template('login.html')
    if request.method == 'POST':
        ip = request.form['defend_ip']
        ip = Defend.waffilter(ip)  # 过滤处理
        result = dangerous_manageCharts.dealdangerbyself(ip)
        if result == 0:
            print(ip + " 防御失败")

    defend_index_list = []
    length, ip_list, country_name, country_specificname, city_name, time = ip_manageCharts.selectalllistCharts()
    for i in ip_list:
        defend_index = dangerous_manageCharts.selectisdeal(i)
        defend_index_list.append(defend_index)
        # info_list.append("已防御")
    # print(defend_index_list)
    ipcountry_pie, foreign_num = ip_manageCharts.selectby_countryCharts()
    ipcity_pie, china_num = ip_manageCharts.selectby_chinacityCharts()
    earthmapcharts = earthMapCharts.earthMap()
    dangerBar = dangerous_manageCharts.dangerBarCharts()

    return render_template('manage/ipmanage.html',
                           ipcountry_pie=ipcountry_pie.render_embed(),
                           ipcity_pie=ipcity_pie.render_embed(),
                           foreign_num=foreign_num,
                           china_num=china_num,
                           length=length,
                           ip_list=ip_list,
                           country_name=country_name,
                           country_specificname=country_specificname,
                           city_name=city_name,
                           time=time,
                           index_list=defend_index_list,
                           earthmapcharts=earthmapcharts.render_embed(),
                           dangerBar=dangerBar.render_embed(),
                           )


# 发送邮箱，用于告警
mail = Mail(app)


# @app.route('/sendEmail')
# def sendEmail():
#     msg = Message(subject='服务器遭受攻击',sender='yoursender@qq.com',recipients=['2534395766@qq.com'])
#     msg.body = '您的服务器正遭受攻击，请前往态势感知系统查看！！'
#     msg.html = '<b>您的服务器正遭受攻击，请前往态势感知系统查看！！</b> '
#     mail.send(msg)
#     return '邮件发送成功'


#
# @app.route('/test',methods=['GET','POST'])
# def testhtml():
#     # return render_template("test.html")


# 原始数据
@app.route('/get_raw_data', methods=['GET', 'POST'])
def get_raw_data():
    if session.get('username') != 'admin':
        return render_template('login.html')
    ip = request.args.get('ip')
    ip = Defend.waffilter(ip)  # 过滤处理
    event_num = event_manageCharts.dealevent_numCharts(ip)
    length = len(event_num)
    apache_raw, ssh_raw, network_raw = event_manage.getraw_data(ip)
    print(apache_raw, ssh_raw, network_raw)
    return render_template("manage/raw_data.html",
                           event_num=event_num,
                           length=length,
                           ssh_raw=ssh_raw,
                           apache_raw=apache_raw,
                           network_raw=network_raw,
                           ip=ip,
                           )


# @app.route('/danger',methods=['GET','POST'])
# def danger():
#     result=dangerous_manage.check()
#     if result:
#         return redirect(url_for('sendEmail'))
#     return 0

# @app.route('/ip',methods=['GET'])
# def localbyip():
#     ip=request.args.get('ip')
#     ipanalyse.seperate_ip(ip)
#     return 'ip存入'
#
# @app.route('/ssh',methods=['GET'])
# def ssh():
#     sshanalyse.analyseByfile()
#     return 'ssh存入'
#
# @app.route('/apache',methods=['GET'])
# def apache():
#     apacheanalyse.apacheanalyse()
#     return 'apache存入'

# #系统设置
# @app.route('/config',methods=['GET'])
# def config():
#     return 'dd'

# 面板首页
@app.route('/index', methods=['GET', 'POST'])
def index():
    if session.get('username') != 'admin':
        return render_template('login.html')
    # 图表绘制
    # sshanalyse.analyseByfile()
    # apacheanalyse.apacheanalyse()
    apachecharts = apacheCharts.apachePieCharts()
    apache_id = apachecharts._chart_id
    earthmapcharts = earthMapCharts.earthMap()
    earthmap_id = earthmapcharts._chart_id
    sshcharts, risk_index = sshCharts.sshPieCharts()
    sshcharts_id = sshcharts._chart_id
    networkcharts = networkCharts.networkcharts()  # 饼状图
    networkcharts_id = networkcharts.chart_id
    streamcharts = networkCharts.streamcharts()
    processcharts = processCharts.processCharts()
    ip_list, time_list, type_list = attackeventCharts.selectevent()
    flag = 0
    for i in type_list:
        # print(i)
        if i == '木马后门' or i == 'SQL注入':
            flag = 1
        else:
            pass
    if flag == 1:
        msg = Message(subject='服务器遭受攻击', sender='yoursender@qq.com', recipients=['2534395766@qq.com'])
        msg.body = '您的服务器正遭受攻击，请前往态势感知系统查看！！'
        msg.html = '<b>您的服务器正遭受攻击，请前往态势感知系统查看！！</b> '
        mail.send(msg)
    else:
        pass

    length = len(ip_list)
    return render_template('base.html',
                           apachecharts=apachecharts.render_embed(),
                           apache_id=apache_id,
                           earthmapcharts=earthmapcharts.render_embed(),
                           earthmap_id=earthmap_id,
                           sshcharts=sshcharts.render_embed(),
                           sshcharts_id=sshcharts_id,
                           # gauge=gauge.render_embed(),
                           networkcharts=networkcharts.render_embed(),
                           networkcharts_id=networkcharts_id,
                           streamcharts=streamcharts.render_embed(),
                           processcharts=processcharts.render_embed(),
                           risk_index=risk_index,
                           ip_list=ip_list,
                           time_list=time_list,
                           type_list=type_list,
                           length=length,
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
