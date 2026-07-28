import json
import os

class Storage:
    def __init__(self, file_path="tasks.json"):
        # 默认将数据保存在当前目录的 tasks.json 文件中
        self.file_path = file_path

    def load_tasks(self):
        """从电脑硬盘读取任务"""
        # 如果文件还不存在（比如第一次运行），就返回一个空列表
        if not os.path.exists(self.file_path):
            return []
        
        # 打开并读取 JSON 文件
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_tasks(self, tasks):
        """将任务列表保存到电脑硬盘"""
        # 以覆盖写入模式（"w"）打开文件，保存数据
        with open(self.file_path, "w", encoding="utf-8") as f:
            # indent=4 是为了让保存在文件里的 JSON 代码自动换行对齐，方便人类阅读
            json.dump(tasks, f, ensure_ascii=False, indent=4)