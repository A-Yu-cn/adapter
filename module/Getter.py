import logging
from threading import Thread
from time import sleep
from dotenv import find_dotenv, load_dotenv
import os
from imbox import Imbox
from jinja2 import Template

from module.sendBuffer import sendList

load_dotenv(find_dotenv(), encoding="utf8")


def machining(message):
    """
    对获取到的邮件信息进行处理，将处理后的信息放入发送队列中
    :param message:获取到的邮箱信息
    :return: 返回为空，直接在函数内将处理好要发送的信息封装放入发送队列了
    """
    with open(os.environ.get("LINE_TEMPLATE_FILE"), 'r', encoding="utf8") as f:
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
    if num == -1:  # 无法匹配字符串代表发送的不是流水线相关信息，直接跳过即可。
        return
    else:
        text = text[num + 56:num + 300]
        str_l = text.split('[')[1].split(']')
        line = str_l[0]
        text = str_l[1]
        res = text[7:9]
        text = text.split('"')
        link = text[1]
        # 上述代码经过测试对华为云平台发送的信息可以完全符号
        data["title"] = "流水线通知:生成" + res
        data["markdown"]["text"] = template.render({
            "stream_line": line,
            "res": res,
            "link": link
        })
        sendList.put({"data": data, "type": 2})


def getter():
    """
    自动从邮箱读取未读邮件，并将其置为已读防止下一次误读操作
    :return:无
    """
    password = os.environ.get("password")
    # IMAP服务器地址，邮箱地址，密码，是否打开SSL加密
    while 1:
        try:
            # 经验判断差不多需要30秒才不会使得远程主机强制关闭连接

            with Imbox(os.environ.get("imap_server"), os.environ.get("email"), password, ssl=False) as imbox:
                # 查询所有未读消息
                all_box_messages = imbox.messages(unread=True)
                for uid, message in all_box_messages:
                    # 对获取到的邮箱数据进行加工
                    machining(message)
                    # 最后将邮件标记为已读
                    imbox.mark_seen(uid)
            sleep(30)
        except Exception as e:
            logging.error("服务器获取信息错误" + str(e))


def run_getter():
    """
    启动一个getter函数的线程，在主函数结束后会自动结束
    :return:无返回值
    """
    try:
        t = Thread(target=getter)
        t.setDaemon(True)
        t.start()
    except Exception as e:
        logging.error("无法接收启动线程" + str(e))
