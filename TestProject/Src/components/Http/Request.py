import requests
from Abnormal.UrlAbnormal import UrlAbnormal


class Request:
    '''
    请求基类
    '''

    def __init__(self, beforRequest: "请求前可以执行一段自定义代码", afterRequest: "请求后可以执行一段自定义代码"):
        self.beforRequest = beforRequest
        self.afterRequest = afterRequest
        self.Header = None
        self.cookie = None
        self.baseHost = None

    def Post(self, url: str, paramter=None):
        '''
        Post请求
        '''
        self.request("Post", url, paramter)

    def Get(self, url: str, paramter=None):
        '''
        Get请求
        '''
        self.request("Get", url, paramter)

    def Put(self, url: str, paramter=None):
        '''
        Put请求
        '''
        self.request("Put", url, paramter)

    def Head(self, url: str):
        '''
        Head请求
        '''
        self.request("Head", url)

    def Options(self, url: str):
        '''
        Options请求
        '''
        self.request("Options", url)

    def Delete(self, url: str):
        '''
        Delete请求
        '''
        self.request("Delete", url)

    def RequiredUrl(self, url):
        '''
        Url验证
        '''
        if not url:
            raise(UrlAbnormal())

    def request(self, method: "支持Post、Get、Put、Head、Options、Delete", url: str, paramter=None):
        '''
        基础请求
        '''
        self.RequiredUrl(url)
        self.beforRequest(self)
        switch = {
            "Post": requests.post(self.baseHost+url, paramter, headers=self.Header, cookies=self.cookie),
            "Get": requests.get(self.baseHost+url, paramter, headers=self.Header, cookies=self.cookie),
            "Put": requests.put(self.baseHost+url, paramter, headers=self.Header, cookies=self.cookie),
            "Head": requests.head(self.baseHost+url, headers=self.Header, cookies=self.cookie),
            "Options": requests.options(self.baseHost+url, headers=self.Header, cookies=self.cookie),
            "Delete": requests.delete(self.baseHost+url, headers=self.Header, cookies=self.cookie)
        }
        self.afterRequest(switch[method], self)


if __name__ == "__main__":
    def befor(req):
        req.Header = {}
        req.cookie = ""
        req.baseHost = "http://baidu.com"

    def aftr(resp, req):
        print(resp.text)
    print(Request(befor, aftr).Get("/"))
