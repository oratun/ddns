# 阿里云动态域名
Python 脚本定时访问第三方接口，获取路由器公网IP，
判断公网ip是否变化，如果改变则修改调用阿里云SDK修改域名解析记录。
# 前提条件
- 宽带有公网ip
- 阿里云购买的域名
- 阿里云控制台
    - RAM访问控制-创建用户并分配DNS相关资源的权限
    - 获取accessId和key等信息

# Python 依赖
```
aliyun-python-sdk-alidns 2.6.18 
aliyunsdkcore            1.0.3  
```

**Crontab 定时任务**
```sh
# 每30分钟运行
*/30 * * * * /Users/oratun/code/ddns/aliyun.sh >> /Users/oratun/code/ddns/ddns.log 2>&1
```