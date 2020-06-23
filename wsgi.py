#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))

# 引入 app.py
import app

# 必须有一个叫做 application 的变量
# gunicorn 就要这个变量
# 这个变量的值必须是 Flask 实例
# 这是规定的套路(协议)
application = app.app

# 这是把代码部署到 apache gunicorn nginx 后面的套路
"""
配置nginx
mkdir /etc/nginx/sites-available
mkdir /etc/nginx/sites-enabled

修改nginx配置文件 /etc/nginx/nginx.conf 使其包含符号链接虚拟主机文件，在 http {} 区块结束前加上如下内容：
include /etc/nginx/sites-enabled/*.nginx;

配置软链接到 /etc/nginx/sites-available  /etc/nginx/sites-enabled
systemctl restart nginx


配置方法已经更改 centos7安装supervisor详细教程 https://www.jianshu.com/p/8605fcdb1138
gunicorn wsgi --bind 0.0.0.0:2000
➜  ~ cat /etc/supervisor/conf.d/xx.conf

[program:todo]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2000 --pid /tmp/todo.pid
directory=/root/web13
autostart=true
"""