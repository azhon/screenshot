import os
import subprocess
import time
import platform


# 截取设备的名字串
def handler_name(device_name):
    return device_name.split("\t")[0]


class adb():

    def __init__(self):
        # 获取主程序执行的路径
        main_dir = os.getcwd()
        # 拼接路径
        if platform.system() == 'Windows':
            self.adb_path = os.path.join(main_dir, "tools", 'adb.exe')
            # 系统的换行符号
            self.enter_char = '\r\n'
        else:
            self.adb_path = os.path.join(main_dir, "tools", 'adb')
            self.enter_char = '\n'

        # 保存所有已连接的设备
        self.all_device = []
        self.adb_version()

    def adb_version(self):
        # 获取当前adb的版本号
        result = self.run("version").split(self.enter_char)
        print("ADB版本信息：\n\t", result[0])

        self.has_device()
        pass

    def has_device(self):
        has_device = False
        while not has_device:
            result = self.run("devices")
            if result == ('List of devices attached' + self.enter_char + self.enter_char):
                print("请连接Android设备...")
            else:
                # 找到了设备
                print("找到以下设备：")
                devices = result.split(self.enter_char)
                all_device = []
                index = 0
                for device in devices:
                    # 获取所有设备
                    if device.endswith('device') or device.endswith('unauthorized'):
                        # 去除\t
                        all_device.append(handler_name(device))
                        print('\t设备序号：%d\t设备名称：%s' % (index, device))
                        has_device = True
                        index += 1
                self.all_device = all_device
            time.sleep(3)

    """ 
    执行adb命令
    最终拼接成 adb version/devices   
    """

    def run(self, cmd):
        # Mac平台需要指定shell=True
        process = subprocess.Popen(self.adb_path + " " + cmd, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, shell=True)
        output = process.communicate()
        return output[0].decode('utf8')

    def get_adb_path(self):
        return self.adb_path

    def get_devices(self):
        return self.all_device
