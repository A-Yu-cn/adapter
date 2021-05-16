import requests


class Sender:
    url = 'https://oapi.dingtalk.com/robot/send?access_token=2c28123072f6347d24f0c7406303daa8f494e897ca71809856e4c29a0d6f42d4 '

    def post(self, msg):
        try:
            r = requests.post(self.url, json=msg)
            print(r.content)
            print(r.status_code)
        except():
            print("post error!!")
