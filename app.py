# -*- coding:utf-8 -*-
from threading import Thread

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from admin import user,ipanalyse,sshanalyse,networkanalyse,processanalyse
from charts import apacheCharts,earthMapCharts,sshCharts,networkCharts,processCharts

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


#登录面板
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']
        info=user.check(str(username),str(password))
        return info
    else:
        return render_template('login.html')

#分析ip，结果存入数据库
@app.route('/ip',methods=['GET'])
def localbyip():
    ip=request.args.get('ip')
    ipanalyse.seperate_ip(ip)
    return 'ip存入'

@app.route('/ssh',methods=['GET'])
def ssh():
    sshanalyse.analyseByfile()
    return 'ssh存入'

@app.route('/apache',methods=['GET'])
def apache():
    sshanalyse.analyseByfile()
    return 'apache存入'


#面板首页
@app.route('/',methods=['GET','POST'])
def index():
    #图表绘制
    apachecharts=apacheCharts.apachePieCharts()
    apache_id = apachecharts._chart_id
    earthmapcharts=earthMapCharts.earthMap()
    earthmap_id=earthmapcharts._chart_id
    sshcharts,risk_index=sshCharts.sshPieCharts()
    sshcharts_id=sshcharts._chart_id
    networkcharts=networkCharts.networkcharts()#饼状图
    networkcharts_id=networkcharts.chart_id
    streamcharts=networkCharts.streamcharts()
    processcharts=processCharts.processCharts()
    return render_template('base.html',
                           apachecharts=apachecharts.render_embed(),
                           apache_id=apache_id,
                           earthmapcharts=earthmapcharts.render_embed(),
                           earthmap_id=earthmap_id,
                           sshcharts=sshcharts.render_embed(),
                           sshcharts_id=sshcharts_id,
                           networkcharts=networkcharts.render_embed(),
                           networkcharts_id=networkcharts_id,
                           streamcharts=streamcharts.render_embed(),
                           processcharts=processcharts.render_embed(),
                           risk_index=risk_index,
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
