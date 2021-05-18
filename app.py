from flask import Flask
from module.adapter import Adapter
from flask_restful import Api
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv(), encoding="utf8")

app = Flask(__name__)
api = Api(app)

# 注册路径
api.add_resource(Adapter, '/api/webhook')

if __name__ == '__main__':
    # 在某一端口运行程序
    port = os.environ.get("PORT")
    host = os.environ.get("HOST")
    app.run(port=port, host=host)
