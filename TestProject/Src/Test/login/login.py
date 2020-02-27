import json
from HttpConfig import Config
from BusinessHttp import BusinessHttp


class Login(BusinessHttp):
    def __init__(self, url, data, method):
        super().__init__(url, data, method)
        self.Project = "OPPOProject"

    # def after(self, resp, req):
    #     if resp.ok:
    #         Responsetext = resp.text
    #         if Responsetext.startswith(u'\ufeff'):
    #             Responsetext = Responsetext.encode('utf8')[3:].decode('utf8')
    #         dic = json.loads(Responsetext, encoding=resp.apparent_encoding)
    #         if (dic["code"] == 0):
    #             Config[self.Project]["Header"] = {
    #                 "Authorization":
    #                 "basic %s" % (dic["result"]["access_token"])
    #             }
    #             print(Config[self.Project]["Header"])
    #         else:
    #             print(dic)
