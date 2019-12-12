from Request import Request

from Config.HttpConfig import Config
from components.Pressure.pressure import Pressure
from components.Abnormal.NoneException import NoneException


class ConvenienceHttp(Request):
    def __init__(self, url: "请求路径", data: "请求参数", method: "请求方式"):
        super().__init__(self.befor, self.baseAfter)
        self.url = url
        self.data = data
        self.method = method
        self.RequestStatus = 0
        self.Project=None

    def befor(self, req: "当前请求相关信息(当前对象)"):
        '''
        请求前执行函数
        '''
        if self.Project is None:
            raise(NoneException("Project"))
        req.Header = Config[self.Project]['Header']
        req.cookie = Config[self.Project]['cookie']
        req.baseHost =Config[self.Project]['baseHost'] 

    def baseAfter(self, resp: "当前请求返回相关信息", req: "当前请求相关信息(当前对象)"):
        '''
        基类必须记录当前请求返回的状态
        '''
        if(resp.ok):
            self.RequestStatus = 1
        else:
            self.RequestStatus = -1
        self.after(resp, req)

    def after(self, resp: "当前请求返回相关信息", req: "当前请求相关信息(当前对象)"):
        '''
        请求后执行函数
        需要在子类中实现
        '''
        pass

    def PressureRequest(self, count: int = 100):
        '''
        压测实现默认请求100次
        '''
        pressure = Pressure()
        pressure.Run(self.DoRequest, self.method, self.PressureAfter, count)
        return pressure

    def DoRequest(self, method: "请求方式"):
        '''
        发起请求
        '''
        self.request(method, self.url, self.data)

    def PressureAfter(self, parameter, thread):
        '''
        单个线程请求完成后执行函数
        '''
        print("线程%s已完成耗时%f" % (thread.id, thread.timeConsuming))
