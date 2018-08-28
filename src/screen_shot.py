import datetime


class screen_shot():
    """
    adb adb对象
    save_path 截图保存的路径
    delete_shot 截图完成是否需要删除手机上的截图
    """

    def screen_shot(self, adb, device, save_path, delete_shot):
        file_name = self.get_file_name()
        # 截图
        screen_cap = adb.run("-s " + device + " shell screencap -p /sdcard/" + file_name)
        print(screen_cap)
        adb.run("-s " + device + " pull /sdcard/" + file_name + " " + save_path)
        # 删除截图
        if delete_shot:
            adb.run("shell rm /sdcard/" + file_name)
        print("截图成功文件已保存至：" + save_path + file_name)
        pass

    def get_file_name(self):
        return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
