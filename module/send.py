import requests
import logging


class Sender:
    url = 'https://oapi.dingtalk.com/robot/send?access_token' \
          '=2c28123072f6347d24f0c7406303daa8f494e897ca71809856e4c29a0d6f42d4 '

    @classmethod
    def post(cls, msg):
        try:
            r = requests.post(cls.url, json=msg)
            logging.info("Successfully send message to Ding Ding")
        except Exception as e:
            logging.error(e)
