# Situational-Awareness 态势感知系统

参考：https://github.com/lw1988/PyAwearnessSystem

态势感知系统，基于python和flask，期望能同时在windows和linux上运行

2022-02-07 更新登录功能

2022-02-08 修复了登录时因找不到用户名而500的错误，但存在任意不存在用户/0登录的情况

2022-02-08 增加了ip分析和ssh分析的情况，结果存入数据库

2022-02-09 增加apache日志分析，结果存入数据库，目前只分析了目录遍历和爆破

2022-02-10 完成ssh图表可视化和世界攻击ip流向图，如下：

![image](https://user-images.githubusercontent.com/78641812/153380881-01a38f14-0335-43b6-9ef9-d65d7768c76a.png)

![image](https://user-images.githubusercontent.com/78641812/153381904-08ac98da-94bc-4138-8ba4-d10d76e85290.png)

2022-03-09 增加了流量分析代码，目前对http和https以及ddos攻击进行分析

2022-03-11 绘制进出口流量图表和流量攻击类型统计饼图，如下：

![image](https://user-images.githubusercontent.com/78641812/157826576-add73af5-2999-46d9-b6ab-1896f8a794e7.png)

2022-03-14 前端整理中，效果图暂时如下（还未完善左边）

![image](https://user-images.githubusercontent.com/78641812/158146651-d441c5d8-3fc5-4db5-90c6-8cc2fd024a37.png)

2022-03-16 前端整理中，效果图如下

![image](https://user-images.githubusercontent.com/78641812/158563462-2d6966e6-5431-42e2-aff0-88630c64a438.png)

2022-03-17 前端整理完成，如下：

![image](https://user-images.githubusercontent.com/78641812/158773590-d43a1b63-ecd8-4431-958f-240ad318d80d.png)

2022-4-03 新增登录界面，修复任意用户登录的bug

![image](https://user-images.githubusercontent.com/78641812/161430621-4e3c5ba7-e996-403b-8bd2-71e9912467a2.png)


2022-4-08 
后端新增功能
1.ip管理

![image](https://user-images.githubusercontent.com/78641812/162403115-8d5dc0b8-edcf-417c-b997-162183747194.png)

2.自动告警，通过发送邮箱实现自动告警，基本功能实现，但是不完全自动，正在修改。

3.原始数据查看
后端算法已上传，前端未写


前端修改：
增加菜单：
![image](https://user-images.githubusercontent.com/78641812/162403401-61476bd0-8a89-4a8a-bb6a-89e1a20006d1.png)

![image](https://user-images.githubusercontent.com/78641812/162403424-bbae7ccf-f054-49ba-8f1a-57123e9c2956.png)

整体样式未调整

2022-4-09

安装bug说明：
请勿安装jinja2最新版本（3.1.1），3.1.1对markup进行了破坏，可能会无法渲染前端

后端功能：
1.自动告警bug修复
2.主动/被动防御功能增加


至此核心功能已经大致增加完毕，明天开始前端整理

2022-4-10
1.登录界面样式更换：
![image](https://user-images.githubusercontent.com/78641812/162612427-1a18f144-40fa-48ed-b123-b22211ccc0dc.png)

2.ip管理页面前端整理，如下：
![image](https://user-images.githubusercontent.com/78641812/162612451-31ac6a4c-8e5c-4219-b195-185d209272ca.png)

![image](https://user-images.githubusercontent.com/78641812/162619983-eb0eaeca-b6c7-436d-a92d-b019291f92ef.png)

ip管理页面大概就这样了，本来还想增加一些功能，但是前端实在是太折磨人了，先就这样了。

自动告警存在的bug为：运行后置执行一次，这里涉及到线程，（当时逃课了，所以我不知道怎么才能让他一直运行又不卡死，等待学习ing........QAQ）

2022-4-11

1.ip管理页面前端整理如下：

![image](https://user-images.githubusercontent.com/78641812/162699187-6f46d6ff-9e4c-49a8-a3e1-383b66e5b90b.png)

![image](https://user-images.githubusercontent.com/78641812/162699338-5f5cfca2-576e-47e3-8614-508b264cd27c.png)


2022-4-13
后端：
权限管理增加，密码修改功能增加

前端

1.原始数据页面前端整理

![image](https://user-images.githubusercontent.com/78641812/163164688-e4d2d8e8-f558-4cae-b2c4-d1bbbe7e41b5.png)


![image](https://user-images.githubusercontent.com/78641812/163164645-44510807-eada-4c17-89e9-819772957b49.png)


2.密码修改前端整理完成

![image](https://user-images.githubusercontent.com/78641812/163181033-7493a291-67e9-40ca-b9e2-6da9dd70644b.png)


功能已经全部完善。

2022-11-14
没想到随便写的系统会受到这么多人关注，所以想对这个系统进行升级和维护，今天先打包所有文件到release，预期一个月上线V2.0
