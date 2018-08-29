### Android设备截屏神器

只需要一根数据线将手机连上电脑（已打开USB调式并已允许调试）
便可以在电脑上轻松的对手机进行截屏了，再也不需要先截个图然后登录个QQor微信将截屏发送至电脑了。
同时支持`Windows`和`Mac`平台哦
 
#### 需要安装Python3.7

  不会安装的话网上找找教程，在配置个环境变量
	
#### 进入到`screenshot`目录 使用python执行`__main__.py`运行程序

```
$ python __main__.py
```
#### `/tools/config.json`项目配置文件介绍

```
{ 
  //截图保存在电脑上目录
  "save_path": "/Users/azhon/Desktop/",
  // 截图成功是否删除手机上的截图
  "delete_shot": "true"
}
```

#### 运行效果
<img src="https://github.com/azhon/screenshot/blob/master/img/code_1.png" width="500"/>

 进行截图

<img src="https://github.com/azhon/screenshot/blob/master/img/code_2.png" width="500"/>

#### ps:我觉得测试工程师使用起来应该会倍儿爽，同意的点个star吧  (^-^)
