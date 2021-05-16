from flask import request
from flask_restful import Resource
from send import Sender

"""
    Adapter 用于接收程序收到的各式请求，然后进行不同的处理
    * post方法获取到华为云平台发送的webhook信息
    * 经过处理后调用Sender类的post方法将信息再发送给钉钉的机器人webhook
"""


class Adapter(Resource):
    @staticmethod
    def post():
        print(request.data)
        data = {'name': 'test'}
        Sender.post(data)

    @staticmethod
    def get():
        print(request.values)
        return {"data": "str"}
