import json
from Config.HttpConfig import Config
from components.BusinessHttp import BusinessHttp


class Login(BusinessHttp):
    def __init__(self):
        super().__init__("/api/City/InternationalCityList?str.value=zh", None,
                         "Get")
        self.Project = "OPPOProject"

    def after(self, resp, req):
        if resp.ok:
            Responsetext = resp.text
            if Responsetext.startswith(u'\ufeff'):
                Responsetext = Responsetext.encode('utf8')[3:].decode('utf8')
            dic = json.loads(Responsetext, encoding=resp.apparent_encoding)
            if (dic["code"] == 0):
                Config[self.Project]["Header"] = {
                    "Authorization":
                    "basic %s" % (dic["result"]["access_token"])
                }
                print(Config[self.Project]["Header"])
            else:
                print(dic)
