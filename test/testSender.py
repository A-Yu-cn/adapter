from module.send import Sender
import json

data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "代码检测",
        "text": "# push test message \n - test \n -test too \n "
    },
    "at": {
        "isAtAll": 'true'
    }
}
data1 = {
    "at": {
        "isAtAll": "false"
    },
    "text": {
        "content": "'push 我就是我, 是不一样的烟火"
    },
    "msgtype": "text"
}
if __name__ == "__main__":
    sender = Sender()
    sender.post(data)
