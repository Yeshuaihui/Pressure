class NoneException(Exception):
    # Url为空异常
    def __init__(self,key):
        super().__init__("%s不能为空"%(key))
        self.errorinfo="%s不能为空"%(key)