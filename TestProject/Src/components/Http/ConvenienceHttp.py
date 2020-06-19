from Request import Request
from HttpConfig import Config
from pressure import Pressure
from NoneException import NoneException
from LogComponents import LogComponents
import threading


class ConvenienceHttp(Request):
    def __init__(self, url, data, method):
        super().__init__(self.baseBefor, self.baseAfter)
        self.url = url
        self.data = data
        self.method = method
        self.RequestStatus = 0
        self.Project = None
        self.SuccessAndFailure = list()
        self.lock = threading.Lock()

    def baseBefor(self, req):
        '''
        请求前执行函数
        '''
        if self.Project is None:
            raise (NoneException('Project'))
        req.Header = Config[self.Project]['Header']
        req.cookie = Config[self.Project]['cookie']
        req.baseHost = Config[self.Project]['baseHost']
        self.befor(req)

    def baseAfter(self, resp, req):
        '''
        基类必须记录当前请求返回的状态
        '''
        self.lock.acquire()
        if (resp.ok):
            self.SuccessAndFailure.append(1)
        else:
            self.SuccessAndFailure.append(-1)
        self.lock.release()
        self.after(resp, req)

    def befor(self, req):
        '''
        执行请求前执行函数
        由子类实现
        '''
        pass

    def after(self, resp, req):
        '''
        请求后执行函数
        需要在子类中实现
        '''
        pass

    def PressureRequest(self, count=100):
        '''
        压测实现默认请求100次
        '''
        pressure = Pressure()
        pressure.Run(self.DoRequest, self.method, self.PressureAfter, count)
        return pressure

    def DoRequest(self, method):
        '''
        发起请求
        '''
        return self.request(method, self.url, self.data)

    def PressureAfter(self, parameter, thread):
        '''
        单个线程请求完成后执行函数
        '''
        LogComponents.write('线程%s已完成耗时%f秒' % (thread.id, thread.timeConsuming))

    @property
    def succesSrate(self):
        '''
        成功率
        '''
        return self.SuccessAndFailure.count(1) / len(self.SuccessAndFailure)

    @property
    def failureSrate(self):
        '''
        失败率
        '''
        return self.SuccessAndFailure.count(-1) / len(self.SuccessAndFailure)

    def Duration(self, duration=10, count=100, sleepTime: int = 1):
        '''
        在指定时间内每秒发起count次请求
        '''
        pressure = Pressure()
        return pressure.Duration(duration, self.DoRequest, self.method,
                                 self.PressureAfter, count, sleepTime)

    def DurationAdd(self, duration=10, add=100, sleepTime: int = 1):
        '''
        在指定时间内每秒执行一次压测
        每次压测增加add次请求
        '''
        pressure = Pressure()
        return pressure.DurationAdd(duration, self.DoRequest, self.method,
                                    self.PressureAfter, add, sleepTime)
