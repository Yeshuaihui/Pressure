import sys
import os
import atexit
sys.path.extend([
    os.path.join(root, name)
    for root, dirs, _ in os.walk(os.path.dirname(__file__) + "/../../")
    for name in dirs
])
from login import Login
from pressure import Pressure
from LogComponents import LogComponents


@atexit.register
def atexit_fun():
    LogComponents.getFile().flush()
    LogComponents.getFile().close()


if __name__ == "__main__":
    oppologin = Login(url="/api/City/InternationalCityList?str.value=zh",
                      data=None,
                      method="Get")
    #   oppologin.doBusinessHttp()  # 一次请求
    # press = oppologin.PressureRequest(500)  # 一次压力测试 请求10次
    # press = oppologin.Duration(5, 5)  # 持续压测5次，每次5个请求
    press = oppologin.DurationAdd(10, 2, 1)  # 持续增量压测3次,每隔1秒增加2个请求(第一次请求次数为2)
    print('总时长：%f' % (press.timeSum))  # 总时长
    print('平均时长：%f' % (press.timeAvg))  # 总时长
