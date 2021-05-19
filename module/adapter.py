from flask import request
from flask_restful import Resource
from module.sendBuffer import sendList

import json
import logging
from jinja2 import Template
import os

"""
    此函数只获取字符串最前方的符合ASCII码的字符，因为中文显示有问题因此需要进行一次处理
    输入一串字符串，返回同样是字符串
"""


def split_str(sentence: str) -> str:
    res_str = ''
    for ch in sentence:
        if ord(ch) not in range(0, 255):
            break
        res_str = res_str + ch
    return res_str


def pack_info(sentence: str) -> str:
    return sentence[:25] + "..."


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
            try:
                repository = data.get("repository").get("name")
                repository_url = data.get("repository").get("git_http_url")
            except:
                repository = "None"
                repository_url = "https://12138.site/"
            # print(data)
            name = data.get("user_name")
            # 避免华为云平台推送的请求不符合规范导致以下字段为空
            commits = data.get("commits")
            commits_info = []
            if isinstance(commits, list):
                for commit in commits:
                    commits_info.append({
                        "message": pack_info(split_str(commit.get("message"))),
                        "url": commit.get("url")
                    })
            # 此下定义要返回给钉钉的信息
            user_data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": "代码推送通知",
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
            # 此处插入已经完成，会启动一个线程负责发送信息
            sendList.put(user_data)
            return {
                "result": "ok"
            }
        except Exception as e:
            logging.error(e)

    @staticmethod
    def get():
        # print(request.values)
        return {"data": "str"}
