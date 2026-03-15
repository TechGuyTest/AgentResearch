#!/usr/bin/env python3
"""
任务管理器 - 修复所有 bug 的版本
"""

import json
import time
from datetime import datetime
import copy
import math


# Bug 1: 可变默认参数 - 修复
def create_task(title, description="", tags=None):
    """创建新任务 - 修复了可变默认参数问题"""
    if tags is None:
        tags = []
    task = {
        "id": int(time.time() * 1000),  # 使用毫秒提高唯一性
        "title": title,
        "description": description,
        "tags": tags.copy(),  # 创建副本避免外部修改
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    return task


# Bug 2: 类级别的可变对象 - 修复
class TaskManager:
    """任务管理器类 - 修复了所有 bug"""
    
    def __init__(self, name="默认管理器"):
        self.name = name
        self.all_tasks = []  # 实例属性，不在类级别
        self.completed_count = 0
    
    def add_task(self, task):
        """添加任务到管理器"""
        self.all_tasks.append(task)
        return len(self.all_tasks)
    
    # Bug 3: Late binding closure - 代码已正确（使用默认参数捕获值）
    def create_priority_filters(self):
        """创建优先级过滤器"""
        filters = []
        for priority in ["low", "medium", "high"]:
            def filter_task(task, p=priority):
                return task.get("priority") == p
            filters.append(filter_task)
        return filters
    
    # Bug 4: 修改原始列表 - 修复
    def get_completed_tasks(self):
        """获取已完成的任务 - 不修改原始列表"""
        return [t for t in self.all_tasks if t["completed"]]
    
    # Bug 5: 浮点数比较 - 修复
    def calculate_completion_rate(self):
        """计算完成率 - 使用 math.isclose 避免精度问题"""
        if len(self.all_tasks) == 0:
            return 0.0
        completed = sum(1 for t in self.all_tasks if t["completed"])
        rate = completed / len(self.all_tasks)
        # 使用 math.isclose 比较浮点数
        if math.isclose(rate, 1/3, rel_tol=1e-9):
            print("完成率大约是 1/3")
        return rate
    
    # Bug 6: 资源未正确关闭 - 修复
    def save_to_file(self, filename):
        """保存任务到文件 - 使用 with 语句确保关闭"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.all_tasks, f, indent=2, ensure_ascii=False)
    
    def load_from_file(self, filename):
        """从文件加载任务 - 使用 with 语句确保关闭"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.all_tasks = json.load(f)
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            return False
        return True


# Bug 7: 字符串拼接效率问题 - 修复
def generate_report(tasks):
    """生成任务报告 - 使用列表推导式提高效率"""
    lines = []
    for i, task in enumerate(tasks):
        lines.append(f"任务 {i+1}: {task['title']}")
        lines.append(f"  描述：{task['description']}")
        lines.append(f"  状态：{'已完成' if task['completed'] else '未完成'}")
        lines.append("---")
    return "\n".join(lines)


# Bug 8: 浅拷贝问题 - 修复
def duplicate_tasks(tasks):
    """复制任务列表 - 使用深拷贝"""
    return copy.deepcopy(tasks)


# Bug 9: 异常处理不当 - 修复
def parse_task_date(date_string):
    """解析任务日期 - 只捕获特定异常"""
    try:
        return datetime.fromisoformat(date_string)
    except (ValueError, TypeError) as e:
        print(f"日期解析失败：{e}")
        return None


# Bug 10: 可变参数默认值 + 修改传入参数 - 修复
def add_tags_to_task(task, tags_to_add=None):
    """给任务添加标签 - 不修改原始任务"""
    if tags_to_add is None:
        tags_to_add = []
    
    # 创建新任务对象，不修改原始
    new_task = task.copy()
    new_task["tags"] = task.get("tags", []).copy() + tags_to_add
    return new_task


# Bug 11: 返回值被忽略的陷阱 - 修复
class TaskValidator:
    """任务验证器 - 修复了返回值检查"""
    
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
        """验证整个任务 - 检查返回值"""
        self.errors = []
        # 检查返回值
        if not self.validate_title(task.get("title", "")):
            return False
        # 继续执行其他验证...
        return len(self.errors) == 0


# Bug 12: 列表推导式中的变量泄露 - 代码已正确（Python 3 中没问题）
def find_tasks_by_tag(tasks, target_tag):
    """按标签查找任务"""
    result = [t for t in tasks if target_tag in t.get("tags", [])]
    return result


# Bug 13: 使用 is 比较值 - 修复
def check_task_status(task):
    """检查任务状态 - 使用布尔值直接判断"""
    return "已完成" if task["completed"] else "未完成"


# Bug 14: 未处理的 None 返回值 - 修复
def get_task_by_id(tasks, task_id):
    """按 ID 查找任务 - 明确文档说明可能返回 None"""
    """
    根据任务 ID 查找任务
    
    Args:
        tasks: 任务列表
        task_id: 要查找的任务 ID
    
    Returns:
        找到的任务字典，如果未找到则返回 None
    """
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


# 主程序演示
def main():
    print("=== 任务管理器演示（修复版）===\n")
    
    # 演示修复后的可变默认参数
    print("1. 可变默认参数修复:")
    task1 = create_task("任务 1", tags=["重要"])
    task2 = create_task("任务 2")
    print(f"任务 1 标签：{task1['tags']}")
    print(f"任务 2 标签：{task2['tags']} (现在正确为空!)")
    print()
    
    # 演示修复后的类级别可变对象
    print("2. 类级别可变对象修复:")
    manager1 = TaskManager("管理器 1")
    manager2 = TaskManager("管理器 2")
    manager1.add_task(create_task("独立任务"))
    print(f"管理器 2 的任务数：{len(manager2.all_tasks)} (现在正确为 0!)")
    print()
    
    # 创建一些测试任务
    manager = TaskManager()
    for i in range(3):
        task = create_task(f"测试任务 {i+1}")
        task["completed"] = (i == 0)
        manager.add_task(task)
    
    # 演示修复后的 get_completed_tasks
    print("3. 修改原始列表问题修复:")
    print(f"获取前任务数：{len(manager.all_tasks)}")
    completed = manager.get_completed_tasks()
    print(f"获取后任务数：{len(manager.all_tasks)} (原始列表保持不变!)")
    print()
    
    # 演示修复后的文件操作
    print("4. 文件操作修复:")
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        filename = tmp.name
    manager.save_to_file(filename)
    print(f"文件已保存到 {filename}（正确关闭）")
    print()
    
    # 演示修复后的字符串拼接
    print("5. 字符串拼接效率修复:")
    report = generate_report(manager.all_tasks)
    print("报告已生成（使用高效的列表拼接）")
    print(report[:100] + "...")
    print()
    
    print("=== 演示结束 ===")


if __name__ == "__main__":
    main()
