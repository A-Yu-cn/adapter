from dotenv import find_dotenv, load_dotenv
import os
from imbox import Imbox
from jinja2 import Template

from module.sendBuffer import sendList

load_dotenv(find_dotenv(), encoding="utf8")


def machining(message):
    with open("../message_template.md", 'r', encoding="utf8") as f:
        template = f.read()
    template = Template(template)
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "流水线通知",
            "text": ""
        }
    }
    text = message.body['html'][0]

    # 下述操作为字符串的切割操作，首先定位到需要的部分，然后经过数次符号切割以及相对定位将所有推送需要用到的信息全部获得
    num = text.find('DevCloud软件开发云上有与您相关的“PipeLine”新动态，请查收。')
    name = text[num + 47:num + 56]
    text = text[num + 56:num + 300]
    str_l = text.split('[')[1].split(']')
    line = str_l[0]
    text = str_l[1]
    res = text[7:9]
    str_l = text.split('"')
    link = str_l[1]
    # 上述代码经过测试对华为云平台发送的信息可以完全符号

    data["markdown"]["text"] = template.render({
        "user_name": name,
        "stream_line": line,
        "res": res,
        "link": link
    })
    print(data["markdown"]["text"])
    sendList.put(data)


password = os.environ.get("password")
# IMAP服务器地址，邮箱地址，密码，是否打开SSL加密
with Imbox(os.environ.get("imap_server"), os.environ.get("email"), password, ssl=False) as imbox:
    all_box_messages = imbox.messages(unread=True)
    for uid, message in all_box_messages:
        print(message.subject)
        machining(message)
        imbox.mark_seen(uid)
