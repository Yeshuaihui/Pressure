import threading
import uuid
import time
import random
import datetime


class myThread(threading.Thread):
    '''
    自定义线程类
    可以异步线程执行传入函数并传入指定参数
    最后以函数结果作为参数执行传入的处理结果函数
    '''
    def __init__(self, funExec:"线程执行的函数", paramter:"线程执行函数的参数", resultFun:"函数执行完成返回结果的处理方式", id:"线程id,不传入则使用guid"=None):
        threading.Thread.__init__(self)
        self.funExec = funExec
        self.paramter = paramter
        self.resultFun = resultFun
        self.beginTime = None
        self.endTime = None
        if(id is None):
            self.id = uuid.uuid1()
        else:
            self.id = id

    def run(self):
        '''
        运行线程
        '''
        self.beginTime = datetime.datetime.now()
        result = self.funExec(self.paramter)
        self.endTime = datetime.datetime.now()
        self.resultFun(result, self)

    @property
    def timeConsuming(self):
        '''
        当前线程耗时
        '''
        return (self.endTime-self.beginTime).total_seconds()


if __name__ == "__main__":
    def exec(paramter: str):
        sleeptime=random.randint(1, 10)
        print(sleeptime)
        time.sleep(sleeptime)
        return int(paramter)

    def resultFun(parameter,thread):
        print("耗时%s"%(thread.timeConsuming))
    l = list()
    for i in range(0, 10):
        thread = myThread(exec, str(i), resultFun, i)
        l.append(thread)
    for item in l:
        item.start()
    for item in l:
        item.join()
    print("主程序结束")
