#!/usr/bin/env python3
"""
任务管理器 - 一个包含常见 bug 模式的练习程序
目标：找出并修复代码中的所有问题
"""

import json
import time
from datetime import datetime

# Bug 1: 可变默认参数
def create_task(title, description="", tags=[]):
    """创建新任务"""
    task = {
        "id": int(time.time()),
        "title": title,
        "description": description,
        "tags": tags,
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    return task


# Bug 2: 类级别的可变对象
class TaskManager:
    """任务管理器类"""
    
    # Bug: 类属性使用可变对象
    all_tasks = []
    completed_count = 0
    
    def __init__(self, name="默认管理器"):
        self.name = name
        # Bug 3: 这里应该初始化实例属性，但上面已经定义了类属性
    
    def add_task(self, task):
        """添加任务到管理器"""
        self.all_tasks.append(task)
        return len(self.all_tasks)
    
    # Bug 4: Late binding closure 问题
    def create_priority_filters(self):
        """创建优先级过滤器"""
        filters = []
        for priority in ["low", "medium", "high"]:
            def filter_task(task, p=priority):
                return task.get("priority") == p
            filters.append(filter_task)
        return filters
    
    def get_completed_tasks(self):
        """获取已完成的任务"""
        # Bug 5: 修改了原始列表而不是返回新列表
        completed = self.all_tasks
        self.all_tasks = [t for t in self.all_tasks if not t["completed"]]
        return completed
    
    # Bug 6: 浮点数比较
    def calculate_completion_rate(self):
        """计算完成率"""
        if len(self.all_tasks) == 0:
            return 0.0
        completed = sum(1 for t in self.all_tasks if t["completed"])
        rate = completed / len(self.all_tasks)
        # Bug: 直接比较浮点数
        if rate == 0.3333333333333333:
            print("完成率正好是 1/3")
        return rate
    
    # Bug 7: 资源未正确关闭
    def save_to_file(self, filename):
        """保存任务到文件"""
        f = open(filename, 'w')
        json.dump(self.all_tasks, f, indent=2)
        # Bug: 忘记关闭文件
    
    def load_from_file(self, filename):
        """从文件加载任务"""
        try:
            f = open(filename, 'r')
            self.all_tasks = json.load(f)
            # Bug: 忘记关闭文件
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            # Bug: 异常时文件可能已经打开但未关闭


# Bug 8: 字符串拼接效率问题
def generate_report(tasks):
    """生成任务报告"""
    report = ""
    for i, task in enumerate(tasks):
        report = report + f"任务 {i+1}: {task['title']}\n"
        report = report + f"  描述：{task['description']}\n"
        report = report + f"  状态：{'已完成' if task['completed'] else '未完成'}\n"
        report = report + "---\n"
    return report


# Bug 9: 浅拷贝问题
def duplicate_tasks(tasks):
    """复制任务列表"""
    # Bug: 这只是浅拷贝，内部字典仍然是引用
    return tasks.copy()


# Bug 10: 异常处理不当
def parse_task_date(date_string):
    """解析任务日期"""
    try:
        return datetime.fromisoformat(date_string)
    except:
        # Bug: 过于宽泛的异常捕获，吞掉了所有错误
        return None


# Bug 11: 可变参数默认值 + 修改传入参数
def add_tags_to_task(task, tags_to_add=[]):
    """给任务添加标签"""
    # Bug: 修改了传入的任务对象
    task["tags"].extend(tags_to_add)
    return task


# Bug 12: 返回值被忽略的陷阱
class TaskValidator:
    """任务验证器"""
    
    def __init__(self):
        self.errors = []
    
    def validate_title(self, title):
        """验证标题"""
        if not title:
            self.errors.append("标题不能为空")
            return False
        if len(title) > 100:
            self.errors.append("标题太长")
            return False
        return True
    
    def validate_task(self, task):
        """验证整个任务"""
        self.errors = []
        # Bug: 没有检查 validate_title 的返回值
        self.validate_title(task.get("title"))
        # 继续执行其他验证...
        return len(self.errors) == 0


# Bug 13: 列表推导式中的变量泄露
def find_tasks_by_tag(tasks, target_tag):
    """按标签查找任务"""
    # Bug: 在 Python 2 中列表推导式会泄露变量，Python 3 中好一些
    # 但这是一个常见的反模式示例
    result = [t for t in tasks if target_tag in t.get("tags", [])]
    # t 变量在这里仍然可访问（虽然 Python 3 中作用域有限）
    return result


# Bug 14: 使用 is 比较值而不是类型
def check_task_status(task):
    """检查任务状态"""
    # Bug: 使用 is 比较布尔值（虽然对小整数有效，但是不好的实践）
    if task["completed"] is True:
        return "已完成"
    elif task["completed"] is False:
        return "未完成"
    return "未知"


# Bug 15: 未处理的 None 返回值
def get_task_by_id(tasks, task_id):
    """按 ID 查找任务"""
    for task in tasks:
        if task["id"] == task_id:
            return task
    # Bug: 隐式返回 None，调用者可能不会检查

# 主程序演示
def main():
    print("=== 任务管理器演示 ===\n")
    
    # 演示 Bug 1: 可变默认参数
    print("1. 可变默认参数问题:")
    task1 = create_task("任务 1", tags=["重要"])
    task2 = create_task("任务 2")
    print(f"任务 1 标签：{task1['tags']}")
    print(f"任务 2 标签：{task2['tags']} (应该为空，但可能不是!)")
    print()
    
    # 演示 Bug 2: 类级别可变对象
    print("2. 类级别可变对象问题:")
    manager1 = TaskManager("管理器 1")
    manager2 = TaskManager("管理器 2")
    manager1.add_task(create_task("共享任务"))
    print(f"管理器 2 的任务数：{len(manager2.all_tasks)} (应该是 0，但可能是 1!)")
    print()
    
    # 创建一些测试任务
    manager = TaskManager()
    for i in range(3):
        task = create_task(f"测试任务 {i+1}")
        task["completed"] = (i == 0)
        manager.add_task(task)
    
    # 演示 Bug 5
    print("3. 修改原始列表问题:")
    print(f"获取前任务数：{len(manager.all_tasks)}")
    completed = manager.get_completed_tasks()
    print(f"获取后任务数：{len(manager.all_tasks)} (原始列表被修改了!)")
    print()
    
    # 演示 Bug 7
    print("4. 文件操作问题:")
    manager.save_to_file("/tmp/tasks.json")
    print("文件已保存（但可能未正确关闭）")
    print()
    
    # 演示 Bug 8
    print("5. 字符串拼接效率:")
    report = generate_report(manager.all_tasks)
    print("报告已生成（使用低效的字符串拼接）")
    print()
    
    print("=== 演示结束 ===")
    print("\n请查看 HINTS.md 文件了解所有需要修复的问题!")


if __name__ == "__main__":
    main()
