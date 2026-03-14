#!/usr/bin/env python3
"""
数据处理器 - 一个有练习价值的程序
包含多种常见 bug 模式，用于调试和代码审查练习
"""

import os
import json
from datetime import datetime

# 全局变量 - 可变默认参数陷阱
def load_config(config_path="config.json", cache={}):
    """加载配置文件 - 有可变默认参数问题"""
    if config_path in cache:
        return cache[config_path]
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    cache[config_path] = config
    return config


def calculate_average(numbers):
    """计算平均值 - 缺少边界条件检查"""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_max_value(data_list):
    """查找最大值 - 索引越界风险"""
    max_val = data_list[0]
    max_index = 0
    
    # 从1开始遍历，但如果列表为空会出错
    for i in range(1, len(data_list)):
        if data_list[i] > max_val:
            max_val = data_list[i]
            max_index = i
    
    return max_val, max_index


def process_file_lines(filepath):
    """处理文件行 - 资源泄露和错误处理缺失"""
    file = open(filepath, 'r')
    lines = file.readlines()
    # 忘记关闭文件
    
    results = []
    for line in lines:
        # 没有处理空行
        parts = line.split(',')
        value = int(parts[1])  # 可能 IndexError 或 ValueError
        results.append(value)
    
    return results


def merge_lists(list1, list2):
    """合并列表 - 代码重复和效率问题"""
    result = []
    
    # 重复的代码模式
    for item in list1:
        if item not in result:
            result.append(item)
    
    # 同样的逻辑又写了一遍
    for item in list2:
        if item not in result:
            result.append(item)
    
    return result


def search_item(items, target):
    """搜索项目 - 性能问题（线性搜索 vs 可优化）"""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def format_currency(amount):
    """格式化货币 - 浮点数精度问题"""
    # 直接格式化浮点数会有精度问题
    return f"${amount:.2f}"


def calculate_discount(price, discount_percent):
    """计算折扣 - 缺少输入验证"""
    discount = price * discount_percent / 100
    return price - discount


def read_user_data(user_id):
    """读取用户数据 - SQL 注入风险模拟"""
    # 模拟数据库查询（实际中应使用参数化查询）
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # 这里只是演示，不实际执行
    return query


def process_batch(items, batch_size):
    """批量处理 - 边界条件错误"""
    results = []
    
    # 当 items 长度不是 batch_size 的整数倍时，会丢失最后一批
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        # 如果最后一批小于 batch_size，可能被错误处理
        if len(batch) == batch_size:
            processed = sum(batch) / len(batch)
            results.append(processed)
    
    return results


def validate_email(email):
    """验证邮箱 - 不完整的验证逻辑"""
    # 过于简单的验证，会接受无效邮箱
    if '@' in email:
        return True
    return False


def copy_list(original):
    """复制列表 - 浅拷贝问题"""
    # 这是浅拷贝，嵌套列表会共享引用
    copied = original[:]
    return copied


def get_nested_value(data, keys):
    """获取嵌套值 - 缺少 KeyError 处理"""
    result = data
    for key in keys:
        result = result[key]  # 如果 key 不存在会抛出 KeyError
    return result


def main():
    """主函数 - 演示各种函数的使用"""
    print("=== 数据处理器演示 ===")
    
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
    
    print("\n=== 演示完成 ===")


if __name__ == "__main__":
    main()
