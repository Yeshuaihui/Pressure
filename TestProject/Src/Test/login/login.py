import json
import sys
import os
sys.path.append("..")
sys.path.extend([os.path.join(root, name)
                 for root, dirs, _ in os.walk("../") for name in dirs])
from Config.HttpConfig import Header, cookie
from components.Http.BusinessHttp import BusinessHttp


class Login(BusinessHttp):
    def __init__(self, url, data, method):
        super().__init__(url, data, method)

    def after(self, resp, req):
        if resp.ok:
            dic = json.loads(resp.text)
            if(dic["code"] == 0):
                Header = {"Authorization": "basic %s" %
                          (dic["result"]["access_token"])}
                print(Header)
            else:
                print(dic)


if __name__ == "__main__":
    login = Login(url="/api/account/OppoLogin",
                  data={"uuid": "111111", "firstname": "ceshi", "lastname": "ceshi", "mail": "haijiang.yan@8travelpay.com", "mobile": "15949030544", "approvelno": "ceshi", "level": "3", "ts": "20191211144600", "sign": "c95b5dc0c2c930b4f05a1b9599c506bc"},
                   method="Post")
    # login.doBusinessHttp()
    pressure= login.PressureRequest()
    print("总时长%f"%(pressure.timeSum))
    print("平均时长%f"%(pressure.timeAvg))
