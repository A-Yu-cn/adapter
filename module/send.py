import requests
import logging


class Sender:
    push_url = 'https://oapi.dingtalk.com/robot/send?access_token' \
               '=2c28123072f6347d24f0c7406303daa8f494e897ca71809856e4c29a0d6f42d4 '

    line_url = 'https://oapi.dingtalk.com/robot/send?access_token=8593e' \
               '98e5f610537cc6e66c05c7916f46d38f2315ed84af606af53d62b063d92'

    @classmethod
    def post(cls, msg, type):
        try:
            if type == 1:
                r = requests.post(cls.push_url, json=msg)
            elif type == 2:
                r = requests.post(cls.line_url, json=msg)
            else:
                logging.warning("send error because of wrone type")
            logging.info("Successfully send message to Ding Ding")
        except Exception as e:
            logging.error(e)
