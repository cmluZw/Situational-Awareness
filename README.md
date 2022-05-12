# Situational-Awareness
态势感知系统

## 开发
一个基于linux的态势感知系统，基于python和flask框架开发，项目目录如下：

admin -核心算法
charts -图表生成
model -类
app.py -主文件
config.py -配置文件
install.py -安装文件

## 安装
### 配置
数据库密码默认设置为root/123456789,后台默认初始密码为：admin/123456，apache日志为默认路径
如需修改，请修改install.py和config.py里的数据库密码和路径

### 邮箱密码
如果不需要告警可忽略，需要告警请自行配置config.py里的邮箱和密码（ps:这里的密码是邮箱授权码）

### 环境
适配linux，且由于作者水平有限，中间件只支持apache，确保linux用户权限为root，且安装有iptables防火墙命令（不需要告警可忽略iptables）
python3，pyecharts0.x
**特别说明，在官方给出解决办法之前请勿安装jinja3.1.1，不然会因markup被破坏无法渲染到前端）**

### 命令
在以上基础下，执行以下命令进行安装：
请用python3执行：

`python3 install.py`

在依赖和数据库都安装成功成功后，执行

`python3 app.py`

待控制台输出以下字样即安装成功
`INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

****访问127.0.0.1:5000即可

如需自动告警功能，请cd到admin/manage目录下，执行

`python3 autodefend.py` 

每两小时会自行检查一次，不需请忽略。


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

静态文件可以自行去echarts-maps下载，如有需要，请联系作者本人(#^.^#)

作者qq:2534395766，请备注来意，以便通过 (*^▽^*)

若觉得本项目对你有帮助，可以给作者点个❤嘛~~

