class UrlAbnormal(Exception):
    # Url为空异常
    def __init__(self):
        super().__init__(self)
        self.errorinfo="Url不能为空"