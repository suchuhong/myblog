from flask import Flask

from routes.session_exp import main as session_routes
from routes.blog import main as blog_routes
from routes.index import main as index_routes
from config.config import secret_key
# web framework
# web application
# __main__
app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = secret_key


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
app.register_blueprint(session_routes, url_prefix='/session')
app.register_blueprint(blog_routes, url_prefix='/blog')
app.register_blueprint(index_routes)


# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)

'''
1, routes/index.py 中的 在 flask 中设置 cookie 和 session 的方法
2, routes/session_exp.py 的 session 和 用户登出
3, 用 博客/留言板 来讲解如何拆分任务
4, 开发的常见方法
'''
