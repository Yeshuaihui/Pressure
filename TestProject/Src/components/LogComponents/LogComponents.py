import time
import os
import threading


class LogComponents():
    staticFile = None
    lock = threading.Lock()
    staticTimeStr = None
    file_Name = None

    @staticmethod
    def write(msg, fileName=None):
        LogComponents.lock.acquire()
        LogComponents.getFile(fileName).write("%s\n" % (msg))
        LogComponents.lock.release()

    @staticmethod
    def getFile(fileName=None):
        if LogComponents.staticFile is None:
            if (fileName is None and LogComponents.file_Name is None):
                fileName = "result%s.txt" % (LogComponents.getTimeStr())
                LogComponents.file_Name = fileName
            dirpath = "%s/Src/Test/Result/" % (os.getcwd())
            if (not os.path.exists(dirpath)):
                os.makedirs(dirpath)
            LogComponents.staticFile = open(dirpath + LogComponents.file_Name,
                                            mode="a",
                                            encoding='utf-8')
        return LogComponents.staticFile

    @staticmethod
    def getTimeStr():
        if LogComponents.staticTimeStr is None:
            staticTimeStr = time.strftime("%Y%m%d%H%M%S", time.localtime())
        return staticTimeStr
