import time
import random
import sys
import os
sys.path.append("..")
sys.path.extend([os.path.join(root, name)
                 for root, dirs, _ in os.walk("../") for name in dirs])

from Multithreading.myThread import myThread

class Pressure:
    '''
    多线程执行任务
    '''

    def __init__(self):
        self.listthread = list()
        self.timesum = float(0)

    def Run(self, funExec, paramter, resultFun, execCount=int):
        '''
        多线程执行任务
        '''
        for i in range(1, execCount):
            thread = myThread(funExec, paramter, resultFun, i)
            self.listthread.append(thread)
            thread.start()
        for item in self.listthread:
            item.join()

    @property
    def timeSum(self):
        '''总时长'''
        if(self.timesum):
            return self.timesum
        timesum = float(0)
        for item in self.listthread:
            timesum += item.timeConsuming
        self.timesum = timesum
        return timesum

    @property
    def timeAvg(self):
        '''平均时长'''
        return self.timeSum/len(self.listthread)


if __name__ == "__main__":
    pressure = Pressure()

    def execfun(par):
        time.sleep(random.randint(1, 3))
        return par["a"]+par["b"]

    def resultFun(parameter, thread):
        time.sleep(random.randint(1, 3))
        print("获取到返回值%i   %s" % (parameter, thread.id))
    pressure.Run(execfun,
                 {"a": 1, "b": 2}, resultFun, 100)
