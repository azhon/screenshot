from src.adb import adb
from src.screen_shot import screen_shot
from src.config import config


# 无限循环
def loop(device):
    while True:
        user_answer = input("是否需要截图 y/n：\n")
        if user_answer == 'y':
            shot.screen_shot(adb, device, config.save_path, config.delete_shot)
        elif user_answer == 'n':
            exit(0)
        else:
            print("无法识别你的答案,请重新输入!")
        pass


if __name__ == '__main__':
    # 获取配置
    config = config()

    # 对adb进行初始化
    adb = adb()

    # 获取当前连接了多少台设备
    count = len(adb.get_devices())

    shot = screen_shot()
    if 0 < count <= 1:
        # 取第一个设备
        loop(adb.get_devices()[0])
        pass
    # 有多个设备的时候
    else:
        illegal = True
        while illegal:
            index = input("请输入设备序号来选择截图的设备：\n")
            index = int(index)
            if 0 <= index <= count - 1:
                illegal = False
                loop(adb.get_devices()[index])
            else:
                print("输入的设备序号非法！请重新输入")
