import sys
import os
import atexit  
sys.path.extend([os.path.join(root, name)
                 for root, dirs, _ in os.walk(os.path.dirname(__file__)+"/../../") for name in dirs])           
from login import Login
from pressure import Pressure
from LogComponents import LogComponents


@atexit.register
def atexit_fun():
      LogComponents.getFile().flush()
      LogComponents.getFile().close()

if __name__ == "__main__":
      oppologin = Login(url="/api/account/OppoLogin",
                        data={"uuid": "111111", "firstname": "ceshi", "lastname": "ceshi", "mail": "haijiang.yan@8travelpay.com", "mobile": "15949030544",
                              "approvelno": "ceshi", "level": "3", "ts": "20191212173124", "sign": "7bbdef2912997ee34088466975d9bc7b"},
                        method="Post")
      # oppologin.doBusinessHttp() # 一次请求
      oppologin.PressureRequest(10) # 一次压力测试 请求10次
      # oppologin.Duration(5,5) # 压测5次，每次5个请求
      # oppologin.DurationAdd(3,2,1) # 压测3次,每隔三秒增加2个请求 

