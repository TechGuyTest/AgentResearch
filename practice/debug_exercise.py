#!/usr/bin/env python3
"""
调试练习文件 - Debug Practice Exercise
这个文件包含多个故意的问题，用于调试训练。
请找出并修复所有问题。

问题类型：逻辑错误、边界情况未处理、低效模式、异常处理不当等
"""

# ============================================================
# 问题 1: 可变默认参数陷阱
# 提示：默认参数在函数定义时只计算一次
# ============================================================
def add_item(item, items=[]):
    """
    将项目添加到列表中。
    注意：这个函数有潜在的问题！
    """
    items.append(item)
    return items


# ============================================================
# 问题 2: 边界情况未处理
# 提示：当列表为空时会发生什么？
# ============================================================
def calculate_average(numbers):
    """
    计算数字列表的平均值。
    注意：考虑边界情况！
    """
    total = sum(numbers)
    return total / len(numbers)


# ============================================================
# 问题 3: 低效的列表查找模式
# 提示：在循环中多次查找同一个值
# ============================================================
def find_and_process_items(data_list, target):
    """
    在列表中查找目标值并处理。
    注意：这个实现效率不高！
    """
    results = []
    
    # 低效：每次都重新遍历列表
    if target in data_list:
        index = data_list.index(target)
        results.append(f"Found at index: {index}")
    
    # 低效：再次遍历列表
    if target in data_list:
        count = data_list.count(target)
        results.append(f"Count: {count}")
    
    # 低效：第三次遍历
    if target in data_list:
        first = data_list[0] if data_list else None
        results.append(f"First item: {first}")
    
    return results


# ============================================================
# 问题 4: 逻辑错误 - 错误的比较操作
# 提示：检查条件判断是否正确
# ============================================================
def is_valid_age(age):
    """
    检查年龄是否有效（0-150 岁之间）。
    注意：逻辑运算符可能有问题！
    """
    # 这个条件判断有逻辑错误
    if age < 0 or age > 150:
        return True  # 这里应该返回什么？
    return False


# ============================================================
# 问题 5: 异常处理不当
# 提示：捕获了所有异常但不处理
# ============================================================
def read_config_file(filepath):
    """
    读取配置文件内容。
    注意：异常处理方式有问题！
    """
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    except Exception:
        # 问题：捕获所有异常但不做任何处理，也不返回任何值
        pass


# ============================================================
# 问题 6: 字符串比较陷阱
# 提示：用户输入可能包含空格或大小写不同
# ============================================================
def check_user_command(user_input, expected_command):
    """
    检查用户输入是否匹配预期命令。
    注意：字符串比较需要考虑什么？
    """
    # 问题：直接比较，没有处理空格和大小写
    if user_input == expected_command:
        return True
    return False


# ============================================================
# 问题 7: 循环中的可变对象引用
# 提示：列表中的字典引用问题
# ============================================================
def create_user_records(usernames):
    """
    为每个用户名创建用户记录。
    注意：可变对象的引用问题！
    """
    records = []
    default_record = {"name": "", "active": True, "permissions": []}
    
    for username in usernames:
        # 问题：所有记录都引用同一个字典对象
        record = default_record
        record["name"] = username
        records.append(record)
    
    return records


# ============================================================
# 测试代码
# ============================================================
if __name__ == "__main__":
    print("=== 调试练习测试 ===\n")
    
    # 测试问题 1
    print("测试 1 - 可变默认参数:")
    print(add_item("a"))  # 预期：['a']
    print(add_item("b"))  # 预期：['b']，但实际会是什么？
    print()
    
    # 测试问题 2
    print("测试 2 - 边界情况:")
    try:
        print(calculate_average([1, 2, 3, 4, 5]))  # 预期：3.0
        print(calculate_average([]))  # 会发生什么？
    except Exception as e:
        print(f"错误：{e}")
    print()
    
    # 测试问题 3
    print("测试 3 - 低效查找:")
    print(find_and_process_items([1, 2, 3, 2, 4, 2], 2))
    print()
    
    # 测试问题 4
    print("测试 4 - 逻辑错误:")
    print(f"is_valid_age(25) = {is_valid_age(25)}")  # 预期：True
    print(f"is_valid_age(-5) = {is_valid_age(-5)}")  # 预期：False
    print(f"is_valid_age(200) = {is_valid_age(200)}")  # 预期：False
    print()
    
    # 测试问题 5
    print("测试 5 - 异常处理:")
    result = read_config_file("nonexistent.txt")
    print(f"读取不存在的文件返回：{result}")
    print()
    
    # 测试问题 6
    print("测试 6 - 字符串比较:")
    print(f"check_user_command('  START  ', 'start') = {check_user_command('  START  ', 'start')}")  # 预期：True
    print()
    
    # 测试问题 7
    print("测试 7 - 可变对象引用:")
    users = create_user_records(["Alice", "Bob", "Charlie"])
    print(f"用户记录：{users}")
    # 预期：每个用户有自己的记录
    # 实际：所有用户的名字都会是什么？
