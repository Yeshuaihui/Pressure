from NoneException import NoneException
class UrlAbnormal(NoneException):
    # Url为空异常
    def __init__(self):
        super().__init__(self,"Url")