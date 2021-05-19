from flask import Flask
from module.adapter import Adapter
from flask_restful import Api
from dotenv import find_dotenv, load_dotenv
import os
import logging
from module.sendBuffer import run_thread
load_dotenv(find_dotenv(), encoding="utf8")

# 日志设置
log_file = os.environ.get("LOG_FILE")
if log_file:
    logging.basicConfig(filename=log_file)
logging.basicConfig(format='[%(asctime)s](%(filename)s)  %(message)s', datefmt='%m/%d/%Y %H:%M:%S %p',
                    level='INFO')

app = Flask(__name__)
api = Api(app)

# 注册路径
api.add_resource(Adapter, '/api/webhook')

if __name__ == '__main__':
    # 在某一端口运行程序
    port = os.environ.get("PORT")
    host = os.environ.get("HOST")
    run_thread()
    app.run(port=port, host=host)

