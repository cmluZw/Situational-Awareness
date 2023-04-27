# Situational-Awareness 态势感知系统

参考：https://github.com/lw1988/PyAwearnessSystem

态势感知系统，基于python和flask

2022-11-14
没想到随便写的系统会受到这么多人关注，所以想对这个系统进行升级和维护，原始代码已经打包到release v1.3，此代码使用与学生，个人，学习，等用途，到V1.3原则上不会再更新。<br>
<br>
新系统将加入机器学习，取名Polestar（极星），仓库地址为：https://github.com/cmluZw/Polestar
<br>


# V1.3
# Situational-Awareness
态势感知系统

## 近期发现某公众号未经本人允许私自售卖此系统以牟利，我在此郑重声明，此态势感知系统开源，望某公众号尽快下架作品，或者免费下载且标明作品作者，拒绝一切未经本人允许的商业用途！！！


前提：此系统只是作者学习flask和态势感知时练手的程序，写的不好，望谅解<br>
V1.3已经打包到右边发行里，请自取，请不要吝啬您的点赞QVQ，小小的点赞带给作者大大的快乐

## 开发
一个基于linux的态势感知系统，基于python和flask框架开发，项目目录如下：

· admin -核心算法<br>
· charts -图表生成<br>
· model -类<br>
· app.py -主文件<br>
· config.py -配置文件<br>

## 安装
<b style="color:#F00">请下载右边发行代码</b>，数据库文件situational.sql也在发行里，请提前安装好mysql，apache，并启动<br>

### 配置
数据库密码默认设置为root1/123456789,后台默认初始密码为：admin/123456，apache日志为默认路径<br>
如需修改，请修改config.py里的数据库密码和路径

### 邮箱密码
如果不需要告警可忽略，需要告警请自行配置config.py和app.py里的邮箱和密码（ps:这里的密码是邮箱授权码）

### 环境
适配linux，且由于作者水平有限，中间件只支持apache，确保linux用户权限为root，且安装有iptables防火墙命令（不需要告警可忽略iptables）<br>
python3（最好是3.7-3.9，过低或过高会报奇怪的错误），pyecharts0.x <br>
**特别说明，在官方给出解决办法之前请勿安装jinja3.1.1，不然会因markup被破坏无法渲染到前端）**

### 安装命令
在以上基础下，执行以下命令进行安装：<br>
安装依赖，请用pip3执行：<br>

`pip3 install -r requirements.txt`

安装mysql数据库:<br>
`
sudo apt install  mysql-server
`
<br>创建数据库用户:<br>

`
CREATE USER 'root1'@'localhost' IDENTIFIED BY '123456789';
GRANT ALL ON *.* TO 'root1'@'localhost';
flush privileges;
`
<br>
`
create database situational;
use situational;
source situational.sql;
`

在依赖和数据库都安装成功成功后，执行<br>

`python3 app.py`

待控制台输出以下字样即安装成功<br>
`INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

****访问127.0.0.1:5000即可

如遇报错，请先查看：https://github.com/cmluZw/Situational-Awareness/issues/6

## 使用

对apache网站进行检测，所以如需模拟攻击请攻击服务器上的apache网站。<br>

## 界面展示

### 登录
![image](https://user-images.githubusercontent.com/78641812/163193263-a5f48a04-b4b0-479f-a484-1ba172139e83.png)

### 主页
![image](https://user-images.githubusercontent.com/78641812/163193478-f33ccc19-b8be-4ea4-a71a-77549f3213f3.png)

### ip管理

![image](https://user-images.githubusercontent.com/78641812/163193685-141841e4-8c3f-4dbe-8c4a-81a18f79b243.png)

### 溯源数据

![image](https://user-images.githubusercontent.com/78641812/163193967-2c4ade2b-12d3-4cc2-9139-581677ddc966.png)

### 动态demo效果图

![预览](https://user-images.githubusercontent.com/78641812/163195281-04f3d30f-4b1f-40f0-97c8-e753456f4326.gif)

## 后续和支持

如需测试数据，有bug提交，或是有建议，请联系作者本人(*￣︶￣)

作者qq:2534395766，请备注来意，以便通过 (*^▽^*)

若觉得本项目对你有帮助，可以给作者点个❤嘛~~
