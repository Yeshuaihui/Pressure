# Pressure
* 一个可以很轻松做到压测的python脚本程序

* 测试的Demo可以看TestProject/Src/Test/main.py中

* `login`类型初始化时设置一下基类的`Project`属性以适配更多网络地址可以做测试</br>
 ##### 假如说 在abc.com站点做了一些请求后需要跳转到其他站点aaa.com</br>
 ##### 按照之前的方式是不支持的，所以修改了下配置结构，可以在这个项目中请求到不同的站点</br>

* `login`类中的after是重写父类`ConvenienceHttp`中的`after`

* `after`会在请求完成之后调用一次

* 可以在`after`中做断言之类的操作
## `after`可以在login.py中查看

* 在基类`ConvenienceHttp`中`succesSrate`可以获取到基于http的请求成功率

* 在基类`ConvenienceHttp`中`failureSrate`可以获取到基于http的请求失败率

* 在基类`ConvenienceHttp`中`baseAfter`函数处理了返回如果没问题对当前请求状态的记录可用于统计请求成功与失败信息

* 调用单次请求可以直接创建好对象之后调用`doBusinessHttp()`函数可以发起一次请求

* 如果需要压测的话调用对象的`PressureRequest()`函数默认压100次

* 压测对象中可以拿到`timeSum`【表示压测耗时总量】、`timeAvg`【表示压测的平均耗时】

* 在`ConvenienceHttp`中添加持续性均量压测`Duration`可以设置压测次数，每次压测间隔时长以及每次压测的次数

* 在`ConvenienceHttp`中添加持续性增量压测`DurationAdd`可以设置每次压测增加次数，每次压测间隔时长以及每次压测的次数
## 详细调用方法可以在main.py中查看

* 添加日志记录方法 使用方式为`LogComponents.write("需要记录的日志")`
#### 日志默认存放在Test目录下的Result文件夹中以Result年月日时分秒.txt文件中
#### 如果需要改在其他目录  可以在 程序执行时 调用`LogComponents.getFile("你想要的文件名")`
#### 这时候日志路径存在Test目录下的Result文件夹中`你想要的文件名`里

