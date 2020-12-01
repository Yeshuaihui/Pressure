import time
# import random
# import sys
# import os
import threading
from .myThread import myThread
from .PressureParamter import PressureParamter


class Pressure:
    '''
    多线程执行任务
    '''
    def __init__(self):
        self.listthread = list()
        self.timesum = float(0)
        self.lock = threading.Lock()

    def Run(self, funExec, paramter, resultFun, execCount=int):
        '''
        多线程执行任务
        '''
        for i in range(0, execCount):
            self.lock.acquire()
            thread = myThread(funExec, paramter, resultFun, i)
            self.listthread.append(thread)
            self.lock.release()
            thread.start()
        for item in self.listthread:
            item.join()

    def Duration(self,
                 duration,
                 funExec,
                 paramter,
                 resultFun,
                 execCount=int,
                 sleepTime: int = 1):
        listPressure = list()
        for index in range(0, duration):
            listPressure.append(
                self.DoDuration(index, funExec, paramter, resultFun,
                                execCount))
            if index < duration - 1:
                time.sleep(sleepTime)
        return listPressure

    def DurationAdd(self,
                    duration,
                    funExec,
                    paramter,
                    resultFun,
                    add=int,
                    sleepTime: int = 1):
        listPressure = list()
        initCount = add
        for index in range(0, duration):
            listPressure.append(
                self.DoDuration(index, funExec, paramter, resultFun,
                                initCount))
            initCount += add
            if index < duration - 1:
                time.sleep(sleepTime)
        return listPressure

    def DoRun(self, paramter: PressureParamter):
        self.Run(paramter.funExec, paramter.paramter, paramter.resultFun,
                 paramter.execCount)

    def DoDuration(self, index, funExec, paramter, resultFun, execCount):
        pressure = Pressure()
        print("curr_index%i" % (index))
        pressure.Run(self.DoRun,
                     PressureParamter(funExec, paramter, resultFun, execCount),
                     None, 1)
        return pressure

    @property
    def timeSum(self):
        '''总时长'''
        if (self.timesum):
            return self.timesum
        timesum = float(0)
        for item in self.listthread:
            timesum += item.timeConsuming
        self.timesum = timesum
        return timesum

    @property
    def timeAvg(self):
        '''平均时长'''
        return self.timeSum / len(self.listthread)


# if __name__ == "__main__":
#     pressure = Pressure()

#     def execfun(par):
#         time.sleep(random.randint(1, 3))
#         return par["a"]+par["b"]

#     def resultFun(parameter, thread):
#         time.sleep(random.randint(1, 3))
#         print("获取到返回值%i   %s" % (parameter, thread.id))
#     pressure.Run(execfun,
#                  {"a": 1, "b": 2}, resultFun, 100)
