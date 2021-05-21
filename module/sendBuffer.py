import logging

from module.send import Sender
from threading import Thread
from queue import Queue

sendList = Queue()


def send_message():
    """
        如果全局的发送请求列表中存在数据，则直接将其发送，否则就等待
    """
    while 1:
        user_data = sendList.get()
        Sender.post(user_data["data"], user_data["type"])


def run_sender():
    """
        启动唯一一个发送线程，监控发送列表，在需要操作时进行发送操作
    """
    # 需要注意只有一个发送线程因此不允许多次调用此函数
    try:
        t = Thread(target=send_message)
        t.setDaemon(True)
        t.start()
    except Exception as e:
        logging.error("Error: 无法启动线程" + str(e))
