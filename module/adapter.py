from flask import request
from flask_restful import Resource
from module.send import Sender
import json
import logging
from jinja2 import Template
import os

"""
    Adapter 用于接收程序收到的各式请求，然后进行不同的处理
    * post方法获取到华为云平台发送的webhook信息
    * 经过处理后调用Sender类的post方法将信息再发送给钉钉的机器人webhook
"""


class Adapter(Resource):

    def __init__(self):
        with open(os.environ.get("TEMPLATE_FILE"), 'r', encoding="utf8") as f:
            template = f.read()
        self.template = Template(template)

    def post(self):
        try:
            # 设置默认返回信息
            data = json.loads(request.data)
            branch = data.get("ref").split("/")[-1]
            repository = data.get("repository").get("name")
            repository_url = data.get("repository").get("git_http_url")
            # print(data)
            name = data.get("user_name")
            # 避免华为云平台推送的请求不符合规范导致以下字段为空
            commits = data.get("commits")
            commits_info = []
            if isinstance(commits, list):
                for commit in commits:
                    commits_info.append({
                        "message": commit.get("message")[:10],
                        "url": commit.get("url")
                    })
            # 此下定义要返回给钉钉的信息
            user_data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": "代码检测",
                    "text": ""
                }
            }
            user_data["markdown"]["text"] = self.template.render({
                "repository": repository,
                "branch": branch,
                "commits": commits_info,
                "name": name,
                "repository_url": repository_url
            })
            # 暂时屏蔽推送到钉钉，部署服务器测试华为云平台发送消息是否正常
            Sender.post(user_data)
            # print(text)
            return {
                "result": "ok"
            }
        except Exception as e:
            logging.error(e)

    @staticmethod
    def get():
        # print(request.values)
        return {"data": "str"}
