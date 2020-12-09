import json
from Config.HttpConfig import Config
from components.BusinessHttp import BusinessHttp


class testApi(BusinessHttp):
    def __init__(self):
        super().__init__("/api/Project/ProjectList", {"MallID":None,"Startus":None,"CityId":None,"pageIndex":1,"pageSize":15},
                         "Post")
        self.Project = "xicheng"

    def after(self, resp, req):
        if resp.ok:
            Responsetext = resp.text
            print(Responsetext)
            if Responsetext.startswith(u'\ufeff'):
                Responsetext = Responsetext.encode('utf8')[3:].decode('utf8')
            dic = json.loads(Responsetext)
            print(dic)
            # if (dic["code"] == 0):
            #     Config[self.Project]["Header"] = {
            #         "Authorization":
            #         "basic %s" % (dic["result"]["access_token"])
            #     }
            #     print(Config[self.Project]["Header"])
            # else:
            #     print(dic)
