# Pressure
* 一个可以很轻松做到压测的python脚本程序

* 测试的Demo可以看TestProject/Src/Test/main.py中

* `login`类中的after是重写父类`ConvenienceHttp`中的`after`

* `login`类型初始化时设置一下基类的`Project`属性以适配更多网络地址可以做测试</br>
 ##### 假如说 在abc.com站点做了一些请求后需要跳转到其他站点aaa.com</br>
 ##### 按照之前的方式是不支持的，所以修改了下配置结构，可以在这个项目中请求到不同的站点</br>

* `after`会在请求完成之后调用一次

* 可以在`after`中做断言之类的操作

* 在基类`ConvenienceHttp`中`baseAfter`函数处理了返回如果没问题对当前请求状态的记录可用于统计请求成功与失败信息

* 调用单次请求可以直接创建好对象之后调用`doBusinessHttp()`函数可以发起一次请求

* 如果需要压测的话调用对象的`PressureRequest()`函数默认压100次

* 压测对象中可以拿到`timeSum`【表示压测耗时总量】、`timeAvg`【表示压测的平均耗时】

* 目前压测比较简单 还没做持续性的压测 后面会出
