from flask import Flask
from module.adapter import Adapter
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# 注册路径
api.add_resource(Adapter, '/api/webhook')

if __name__ == '__main__':
    # 在某一端口运行程序
    app.run(port=666, debug=True, host="0.0.0.0")
