import json
from HttpConfig import Config
from BusinessHttp import BusinessHttp
import datetime
import sys
import os

class CreateCase(BusinessHttp):
    def __init__(self):
        now_time =datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        data = {"caseNumber": now_time, "name": "张三诈骗案", "casePath": "D:\\测试目录\\%s\\%s.tmcc"%(now_time,now_time),
                "investigator": "fdsa", "description": "测试", "remark": "测试的", "_casePath": "D:\\测试目录"}
        super().__init__("/case/create", json.dumps(data), "Post")
        self.Project = "ThunderCloud"

    def after(self, resp, req):
        # print(resp)
        if resp.ok:
            Responsetext = resp.text
            if Responsetext.startswith(u'\ufeff'):
                Responsetext = Responsetext.encode('utf8')[3:].decode('utf8')
            # print(Responsetext)
            dic = json.loads(Responsetext, encoding=resp.apparent_encoding)
            # print(dic)
            createEvidence = CreateEvidence(dic["Data"]["case"]["Id"])
            createEvidence.doBusinessHttp()  # 一次请求


class CreateEvidence(BusinessHttp):
 
    def __init__(self, caseid):
        data = {"number": "32111", "name": "测试", "model": "huawei",
                "owner": "测试", "remark": "测试", "caseid": caseid}
        super().__init__("/evidence/create", json.dumps(data), "Post")
        self.Project = "ThunderCloud"
        self.caseId=caseid

    def after(self, resp, req):
        print(resp)
        if resp.ok:
            createtwittertask = CreateTwitterTask(self.caseId)
            createtwittertask.doBusinessHttp()  # 一次请求
            Responsetext = resp.text
            if Responsetext.startswith(u'\ufeff'):
                Responsetext = Responsetext.encode('utf8')[3:].decode('utf8')
            # print(Responsetext)
            # dic = json.loads(Responsetext, encoding=resp.apparent_encoding)
            # if (dic["code"] == 0):
            #     Config[self.Project]["Header"] = {
            #         "Authorization":
            #         "basic %s" % (dic["result"]["access_token"])
            #     }
            #     print(Config[self.Project]["Header"])
            # else:
            #     print(dic)
class CreateTwitterTask(BusinessHttp):
    def __init__(self, caseid):
        data = {"appName": "Twitter",  "caseid": caseid, "eid": 1, "param":
                "{\"type\":\"account\",\"params\":{\"username\":\"hongliantest\",\"content\":[\"message\",\"follow\",\"fans\",\"collect\"],\"userfull\":\"no\",\"proxyType\":\"SYSTEM\",\"proxyHost\":"",\"proxyPort\":""}}"
                }
        super().__init__("/task/create", json.dumps(data), "Post")
        self.Project = "ThunderCloud"

    def after(self, resp, req):
        print(resp.text)
        if resp.ok:
            Responsetext = resp.text
            if Responsetext.startswith(u'\ufeff'):
                Responsetext = Responsetext.encode('utf8')[3:].decode('utf8')
