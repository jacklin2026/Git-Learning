from task import Task
from storage import Storage

def display_menu():
    print("\n" + "="*30)
    print("🚀 极简待办事项管理器 🚀")
    print("="*30)
    print("1. 添加新任务")
    print("2. 查看所有任务")
    print("3. 标记任务为完成")
    print("4. 退出程序")
    print("-" * 30)

def main():
    # 1. 启动档案柜
    storage = Storage()
    # 2. 从硬盘加载历史任务列表
    tasks_data = storage.load_tasks()

    while True:
        display_menu()
        choice = input("👉 请选择操作 (1-4): ")

        if choice == '1':
            title = input("请输入任务标题: ")
            desc = input("请输入任务详情 (可直接回车跳过): ")
            # 调用 task.py 里的模型创建任务
            new_task = Task(title, desc)
            # 将新任务（转为字典格式）加入列表
            tasks_data.append(new_task.to_dict())
            # 调用 storage.py 保存到硬盘
            storage.save_tasks(tasks_data)
            print(f"\n✅ 成功添加任务: {title}")

        elif choice == '2':
            print("\n📋 当前任务列表:")
            if not tasks_data:
                print("   (空空如也，快去添加任务吧~)")
            else:
                for idx, t in enumerate(tasks_data, 1):
                    # 根据状态显示不同的图标
                    status = "[✅ 完成]" if t['is_completed'] else "[⏳ 待办]"
                    print(f"   {idx}. {status} {t['title']} (创建于: {t['created_at']})")

        elif choice == '3':
            if not tasks_data:
                print("\n❌ 列表为空，没有可以完成的任务。")
                continue
            
            try:
                task_idx = int(input("请输入要完成的任务编号: ")) - 1
                if 0 <= task_idx < len(tasks_data):
                    tasks_data[task_idx]['is_completed'] = True
                    storage.save_tasks(tasks_data)
                    print(f"\n🎉 恭喜！任务 '{tasks_data[task_idx]['title']}' 已完成！")
                else:
                    print("\n❌ 找不到这个编号的任务。")
            except ValueError:
                print("\n❌ 格式错误，请输入纯数字编号。")

        elif choice == '4':
            print("\n👋 感谢使用，数据已全部保存，再见！")
            break
        
        else:
            print("\n❌ 无效的输入，请输入 1 到 4 之间的数字。")

if __name__ == "__main__":
    print("start")
    # 学习操作
    main()
    print("5. 删除任务")
    print("end")