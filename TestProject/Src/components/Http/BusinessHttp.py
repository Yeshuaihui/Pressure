from ConvenienceHttp import ConvenienceHttp

class BusinessHttp(ConvenienceHttp):
    def __init__(self, url, data, method):
        super().__init__(url, data, method)
    
    def doBusinessHttp(self):
        '''
        业务请求
        '''
        self.DoRequest(self.method)