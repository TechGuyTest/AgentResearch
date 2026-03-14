#!/usr/bin/env python3
"""
数据处理器 - 一个有练习价值的程序
包含多种常见 bug 模式，用于调试和代码审查练习

运行方式：python3 data_processor_*.py
"""

import os
import json
from datetime import datetime


# ============= Bug 1: 可变默认参数陷阱 =============
def load_config(config_path="config.json", cache={}):
    """加载配置文件 - 有可变默认参数问题"""
    if config_path in cache:
        return cache[config_path]
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    cache[config_path] = config
    return config


# ============= Bug 2: 除零错误 =============
def calculate_average(numbers):
    """计算平均值 - 缺少边界条件检查"""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


# ============= Bug 3: 索引越界 =============
def find_max_value(data_list):
    """查找最大值 - 索引越界风险"""
    max_val = data_list[0]
    max_index = 0
    
    for i in range(1, len(data_list)):
        if data_list[i] > max_val:
            max_val = data_list[i]
            max_index = i
    
    return max_val, max_index


# ============= Bug 4: 资源泄露 + 缺少异常处理 =============
def process_file_lines(filepath):
    """处理文件行 - 资源泄露和错误处理缺失"""
    file = open(filepath, 'r')
    lines = file.readlines()
    # 忘记关闭文件
    
    results = []
    for line in lines:
        parts = line.split(',')
        value = int(parts[1])  # 可能 IndexError 或 ValueError
        results.append(value)
    
    return results


# ============= Bug 5: 代码重复 + 性能问题 =============
def merge_lists(list1, list2):
    """合并列表 - 代码重复和效率问题"""
    result = []
    
    for item in list1:
        if item not in result:
            result.append(item)
    
    for item in list2:
        if item not in result:
            result.append(item)
    
    return result


# ============= Bug 6: 性能问题（线性搜索） =============
def search_item(items, target):
    """搜索项目 - 性能问题"""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


# ============= Bug 7: 浮点数精度问题 =============
def format_currency(amount):
    """格式化货币 - 浮点数精度问题"""
    return f"${amount:.2f}"


# ============= Bug 8: 缺少输入验证 =============
def calculate_discount(price, discount_percent):
    """计算折扣 - 缺少输入验证"""
    discount = price * discount_percent / 100
    return price - discount


# ============= Bug 9: SQL 注入风险 =============
def read_user_data(user_id):
    """读取用户数据 - SQL 注入风险模拟"""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query


# ============= Bug 10: 边界条件错误 =============
def process_batch(items, batch_size):
    """批量处理 - 边界条件错误"""
    results = []
    
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        if len(batch) == batch_size:
            processed = sum(batch) / len(batch)
            results.append(processed)
    
    return results


# ============= Bug 11: 不完整的验证 =============
def validate_email(email):
    """验证邮箱 - 不完整的验证逻辑"""
    if '@' in email:
        return True
    return False


# ============= Bug 12: 浅拷贝问题 =============
def copy_list(original):
    """复制列表 - 浅拷贝问题"""
    copied = original[:]
    return copied


# ============= Bug 13: 缺少 KeyError 处理 =============
def get_nested_value(data, keys):
    """获取嵌套值 - 缺少 KeyError 处理"""
    result = data
    for key in keys:
        result = result[key]
    return result


# ============= Bug 14: 字符串比较问题 =============
def compare_strings(s1, s2):
    """比较字符串 - 可能 None"""
    return s1.lower() == s2.lower()


# ============= Bug 15: 时区问题 =============
def get_timestamp():
    """获取时间戳 - 时区问题"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    """主函数 - 演示各种函数的使用"""
    print("=== 数据处理器演示 ===\n")
    
    # 演示 calculate_average
    numbers = [10, 20, 30, 40, 50]
    avg = calculate_average(numbers)
    print(f"平均值：{avg}")
    
    # 演示 find_max_value
    data = [3, 7, 2, 9, 1, 8]
    max_val, max_idx = find_max_value(data)
    print(f"最大值：{max_val}, 索引：{max_idx}")
    
    # 演示 merge_lists
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    merged = merge_lists(list1, list2)
    print(f"合并列表：{merged}")
    
    # 演示 format_currency
    price = 19.99
    formatted = format_currency(price)
    print(f"价格：{formatted}")
    
    # 演示 calculate_discount
    original_price = 100
    discount = 15
    final_price = calculate_discount(original_price, discount)
    print(f"折扣后价格：{final_price}")
    
    # 演示 validate_email
    emails = ["test@example.com", "invalid", "no@domain", "@missing.local"]
    for email in emails:
        is_valid = validate_email(email)
        print(f"{email}: {'有效' if is_valid else '无效'}")
    
    # 演示 process_batch
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    batch_results = process_batch(items, 3)
    print(f"批量处理结果：{batch_results}")
    
    # 演示 read_user_data
    user_query = read_user_data("1 OR 1=1")
    print(f"SQL 查询：{user_query}")
    
    # 演示 get_nested_value
    nested_data = {"user": {"name": "Alice", "age": 30}}
    name = get_nested_value(nested_data, ["user", "name"])
    print(f"嵌套值：{name}")
    
    # 演示 compare_strings
    result = compare_strings("Hello", "hello")
    print(f"字符串比较：{result}")
    
    # 演示 get_timestamp
    timestamp = get_timestamp()
    print(f"时间戳：{timestamp}")
    
    print("\n=== 演示完成 ===")


if __name__ == "__main__":
    main()
