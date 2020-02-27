class PressureParamter():
    def __init__(self, funExec, paramter, resultFun, execCount=int):
        self.funExec = funExec
        self.paramter = paramter
        self.resultFun = resultFun
        self.execCount = execCount
