from flask import Flask

# 创建 Flask 应用实例
app = Flask(__name__)

# 定义根路由
@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

# 添加更多路由示例
@app.route('/about')
def about():
    return 'This is a simple Flask watchlist application.'

# 启动应用的代码
if __name__ == '__main__':
    app.run(
        host='127.0.0.1',  # 保持为127.0.0.1
        port=8000,        # 改为其他端口
        debug=True
    )