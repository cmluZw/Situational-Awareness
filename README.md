# Situational-Awareness 态势感知系统

态势感知系统，基于python和flask，期望能同时在windows和linux上运行

2022-02-07 更新登录功能

2022-02-08 修复了登录时因找不到用户名而500的错误，但存在任意不存在用户/0登录的情况

2022-02-08 增加了ip分析和ssh分析的情况，结果存入数据库

2022-02-09 增加apache日志分析，结果存入数据库，目前只分析了目录遍历和爆破

2022-02-10 完成ssh图表可视化和世界攻击ip流向图，如下：

![image](https://user-images.githubusercontent.com/78641812/153380881-01a38f14-0335-43b6-9ef9-d65d7768c76a.png)

![image](https://user-images.githubusercontent.com/78641812/153381904-08ac98da-94bc-4138-8ba4-d10d76e85290.png)


