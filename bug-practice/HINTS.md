# Bug 练习程序 - 改进提示

本文件列出了 `buggy_task_manager_*.py` 中所有需要修复的问题。

## 📋 问题清单

### Bug 1: 可变默认参数
**位置**: `create_task()` 函数的 `tags=[]` 参数

**问题**: 使用可变对象（列表）作为默认参数值。所有调用共享同一个列表对象。

**修复方法**:
```python
def create_task(title, description="", tags=None):
    if tags is None:
        tags = []
    # ... 其余代码
```

---

### Bug 2: 类级别的可变对象
**位置**: `TaskManager` 类的 `all_tasks = []` 和 `completed_count = 0`

**问题**: 类属性在所有实例间共享。应该使用实例属性。

**修复方法**:
```python
class TaskManager:
    def __init__(self, name="默认管理器"):
        self.name = name
        self.all_tasks = []
        self.completed_count = 0
```

---

### Bug 3: Late Binding Closure（闭包延迟绑定）
**位置**: `create_priority_filters()` 方法

**问题**: 循环中创建的闭包会捕获变量引用而非值。注意：代码中已经用 `p=priority` 修复了，但原始版本应该是：
```python
# 错误版本
def filter_task(task):
    return task.get("priority") == priority  # 所有过滤器都使用最后的 priority 值
```

**修复方法**: 使用默认参数捕获当前值（代码已展示正确做法）。

---

### Bug 4: 修改原始列表而非返回副本
**位置**: `get_completed_tasks()` 方法

**问题**: 方法意外修改了 `self.all_tasks`，这是副作用。

**修复方法**:
```python
def get_completed_tasks(self):
    return [t for t in self.all_tasks if t["completed"]]
```

---

### Bug 5: 浮点数直接比较
**位置**: `calculate_completion_rate()` 方法

**问题**: 使用 `==` 直接比较浮点数，由于精度问题可能失败。

**修复方法**:
```python
import math
if math.isclose(rate, 1/3, rel_tol=1e-9):
    print("完成率大约是 1/3")
```

---

### Bug 6: 资源未正确关闭
**位置**: `save_to_file()` 和 `load_from_file()` 方法

**问题**: 文件打开后未关闭，可能导致资源泄漏。

**修复方法**: 使用 `with` 语句
```python
def save_to_file(self, filename):
    with open(filename, 'w') as f:
        json.dump(self.all_tasks, f, indent=2)
```

---

### Bug 7: 字符串拼接效率低下
**位置**: `generate_report()` 函数

**问题**: 在循环中使用 `+` 拼接字符串，每次都会创建新字符串对象。

**修复方法**:
```python
def generate_report(tasks):
    lines = []
    for i, task in enumerate(tasks):
        lines.append(f"任务 {i+1}: {task['title']}")
        lines.append(f"  描述：{task['description']}")
        lines.append(f"  状态：{'已完成' if task['completed'] else '未完成'}")
        lines.append("---")
    return "\n".join(lines)
```

---

### Bug 8: 浅拷贝问题
**位置**: `duplicate_tasks()` 函数

**问题**: `list.copy()` 只创建浅拷贝，内部字典仍是引用。

**修复方法**:
```python
import copy
def duplicate_tasks(tasks):
    return copy.deepcopy(tasks)
```

---

### Bug 9: 过于宽泛的异常捕获
**位置**: `parse_task_date()` 函数

**问题**: `except:` 捕获所有异常，包括 `KeyboardInterrupt` 和 `SystemExit`。

**修复方法**:
```python
def parse_task_date(date_string):
    try:
        return datetime.fromisoformat(date_string)
    except (ValueError, TypeError) as e:
        print(f"日期解析失败：{e}")
        return None
```

---

### Bug 10: 修改传入的可变参数
**位置**: `add_tags_to_task()` 函数

**问题**: 函数修改了传入的任务对象，产生意外副作用。

**修复方法**:
```python
def add_tags_to_task(task, tags_to_add=None):
    if tags_to_add is None:
        tags_to_add = []
    # 创建新任务对象
    new_task = task.copy()
    new_task["tags"] = task.get("tags", []) + tags_to_add
    return new_task
```

---

### Bug 11: 忽略返回值
**位置**: `TaskValidator.validate_task()` 方法

**问题**: 调用 `validate_title()` 但没有检查返回值。

**修复方法**:
```python
def validate_task(self, task):
    self.errors = []
    if not self.validate_title(task.get("title")):
        return False
    # 其他验证...
    return len(self.errors) == 0
```

---

### Bug 12: 使用 `is` 比较布尔值
**位置**: `check_task_status()` 函数

**问题**: 虽然对小整数有效，但应该用 `==` 或直接用布尔值。

**修复方法**:
```python
def check_task_status(task):
    return "已完成" if task["completed"] else "未完成"
```

---

### Bug 13: 未处理 None 返回值
**位置**: `get_task_by_id()` 函数

**问题**: 函数可能返回 `None`，调用者可能不会检查。

**修复方法**:
```python
def get_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise ValueError(f"未找到 ID 为 {task_id} 的任务")
# 或返回 Optional[Task] 并在文档中说明
```

---

## 🎯 练习建议

1. **第一步**: 运行程序，观察哪些 bug 会导致明显的错误输出
2. **第二步**: 逐个阅读 HINTS，理解每个问题的原因
3. **第三步**: 创建修复版本 `fixed_task_manager.py`
4. **第四步**: 编写单元测试验证修复
5. **第五步**: 添加类型注解提高代码质量

## 📚 相关知识点

- Python 默认参数求值时机
- 类属性 vs 实例属性
- 闭包和变量捕获
- 可变 vs 不可变对象
- 深拷贝 vs 浅拷贝
- 上下文管理器 (`with` 语句)
- 异常处理最佳实践
- Python 性能优化技巧

---

**创建时间**: 2026-03-14
**难度**: 中级
**预计完成时间**: 60-90 分钟
