import json
import os

"""
获取配置文件
"""


class config():

    def __init__(self):
        # 获取主程序执行的路径
        main_dir = os.getcwd()
        # 拼接路径
        file_config = os.path.join(main_dir, "tools", 'config.json')
        with open(file_config, 'r') as c:
            config = json.load(c)
            # 保存配置
            self.save_path = config['save_path']
            self.delete_shot = config['delete_shot']
