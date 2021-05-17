from flask import request
from flask_restful import Resource
from module.send import Sender
import json

"""
    Adapter 用于接收程序收到的各式请求，然后进行不同的处理
    * post方法获取到华为云平台发送的webhook信息
    * 经过处理后调用Sender类的post方法将信息再发送给钉钉的机器人webhook
"""


class Adapter(Resource):

    @staticmethod
    def post():
        data = json.loads(request.data)
        name = data.get("user_name")
        repository = data.get("project").get("name")
        branch = data.get("project").get("default_branch")
        commit_time = data.get("commits").get("timestamp")
        commit_info = data.get("commits").get("message")
        # 此下定义要返回给钉钉的信息
        user_data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "代码检测",
                "text": ""
            },
            "at": {
                "isAtAll": 'true'
            }
        }
        text = "**代码推送通知** \n  - {name} 推送到了 {repository} / {branch} 分支 \n  - commits:{commit_info} at {commit_time}".format(
            name=name, repository=repository, branch=branch, commit_time=commit_time, commit_info=commit_info)
        user_data["markdown"]["text"] = text
        # 暂时屏蔽推送到钉钉，部署服务器测试华为云平台发送消息是否正常
        Sender.post(user_data)
        print(text)
        return {
            "result": "ok"
        }

    @staticmethod
    def get():
        print(request.values)
        return {"data": "str"}
