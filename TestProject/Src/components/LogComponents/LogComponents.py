import time
import os
import threading

class LogComponents():
    staticFile=None
    lock= threading.Lock()
    staticTimeStr=None
    @staticmethod
    def write(msg,fileName=None):
        LogComponents.lock.acquire()
        LogComponents.getFile(fileName).write("%s\n"%(msg))
        LogComponents.lock.release()
    
    @staticmethod
    def getFile(fileName=None):
        if LogComponents.staticFile is None:
            if(fileName is None):
                fileName="result%s.txt"%(LogComponents.getTimeStr())
            dirpath="%s/TestProject/Src/Test/Result/"%(os.getcwd())
            if(not os.path.exists(dirpath)):
                os.makedirs(dirpath)
            staticFile= open(dirpath+fileName,mode="a",encoding='utf-8')
        return staticFile
    
    @staticmethod
    def getTimeStr():
        if staticTimeStr is None:
            staticTimeStr=time.strftime("%Y%m%d%H%M%S",time.localtime())
        return staticTimeStr