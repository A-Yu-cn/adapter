from module.send import Sender
import logging

data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "代码检测",
        "text": ""
    },
    "at": {
        "isAtAll": 'false'
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
    text = "**代码推送通知** \n  - {name} 推送到了 {repository} / {branch} 分支 \n  - commits:{commit_info} {commit_time}".format(
        name="ayu", repository="fronted", branch="test", commit_time="", commit_info="别看了，这是测试信息")
    data["markdown"]["text"] = text
    sdata = {"data": data, "type": 3}
    try:
        Sender.post(sdata["data"], sdata["type"])
    except Exception as e:
        logging.error(e)
