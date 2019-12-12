
import sys
import os
path = os.path.dirname(__file__)+"/../../" 
sys.path.extend([os.path.join(root, name)
                 for root, dirs, _ in os.walk(path) for name in dirs])
print(os.path.abspath(path))
print(os.path.dirname(__file__))
from login import Login

if __name__ == "__main__":
    oppologin=Login(url="/api/account/OppoLogin",
                  data={"uuid": "111111", "firstname": "ceshi", "lastname": "ceshi", "mail": "haijiang.yan@8travelpay.com", "mobile": "15949030544", "approvelno": "ceshi", "level": "3", "ts": "20191212173124", "sign": "7bbdef2912997ee34088466975d9bc7b"},
                   method="Post")
    oppologin.doBusinessHttp()