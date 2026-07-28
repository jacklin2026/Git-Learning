import uuid
from datetime import datetime

class Task:
    def __init__(self, title, description=""):
        # 自动生成唯一ID和创建时间
        self.id = str(uuid.uuid4())[:8] 
        self.title = title
        self.description = description
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_completed = False

    def mark_completed(self):
        """将任务标记为已完成"""
        self.is_completed = True

    def to_dict(self):
        """将对象转换为字典，方便后续存入 JSON 文件"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "is_completed": self.is_completed
        }
    # 添加备注