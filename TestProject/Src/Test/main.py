
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
                  data={"uuid": "111111", "firstname": "ceshi", "lastname": "ceshi", "mail": "haijiang.yan@8travelpay.com", "mobile": "15949030544", "approvelno": "ceshi", "level": "3", "ts": "20191211144600", "sign": "c95b5dc0c2c930b4f05a1b9599c506bc"},
                   method="Post")
    oppologin.doBusinessHttp()