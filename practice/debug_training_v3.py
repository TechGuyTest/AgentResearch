#!/usr/bin/env python3
"""
Debug Training Exercise v3
==========================
这个文件包含多个故意引入的问题，用于调试训练。
请找出并修复所有问题。

提示：问题类型包括逻辑错误、边界情况未处理、低效模式等。
"""


def calculate_average(numbers):
    """
    计算数字列表的平均值
    
    ⚠️ 问题 1: 边界情况未处理
    提示：当列表为空时会发生什么？
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_maximum(items):
    """
    找到列表中的最大值
    
    ⚠️ 问题 2: 逻辑错误
    提示：初始值设置是否正确？考虑所有元素都是负数的情况。
    """
    max_value = 0  # 这里可能有问题
    for item in items:
        if item > max_value:
            max_value = item
    return max_value


def process_user_data(users):
    """
    处理用户数据，提取活跃用户
    
    ⚠️ 问题 3: 低效模式
    提示：列表查找在循环中是否高效？考虑使用更合适的数据结构。
    """
    active_users = []
    blocked_ids = [5, 10, 15, 20, 25]
    
    for user in users:
        if user['is_active'] and user['id'] not in blocked_ids:
            active_users.append(user)
    
    return active_users


def parse_config(config_string):
    """
    解析配置字符串，格式为 "key=value;key=value"
    
    ⚠️ 问题 4: 异常处理缺失
    提示：如果输入格式不正确会发生什么？考虑空字符串、缺少等号等情况。
    """
    config = {}
    pairs = config_string.split(';')
    
    for pair in pairs:
        key, value = pair.split('=')
        config[key.strip()] = value.strip()
    
    return config


def merge_dicts(dict1, dict2):
    """
    合并两个字典，dict2 的值覆盖 dict1
    
    ⚠️ 问题 5: 副作用问题
    提示：这个函数是否修改了原始字典？这是期望的行为吗？
    """
    result = dict1  # 这里可能有问题
    for key, value in dict2.items():
        result[key] = value
    return result


# ============== 测试代码 ==============

if __name__ == "__main__":
    print("=== Debug Training Exercise ===\n")
    
    # 测试 calculate_average
    print("1. 测试 calculate_average:")
    print(f"   [1, 2, 3, 4, 5] 的平均值: {calculate_average([1, 2, 3, 4, 5])}")
    # print(f"   [] 的平均值: {calculate_average([])}")  # 取消注释会出错
    
    # 测试 find_maximum
    print("\n2. 测试 find_maximum:")
    print(f"   [3, 7, 2, 9, 1] 的最大值: {find_maximum([3, 7, 2, 9, 1])}")
    print(f"   [-5, -2, -9, -1] 的最大值: {find_maximum([-5, -2, -9, -1])}")  # 这个结果对吗？
    
    # 测试 process_user_data
    print("\n3. 测试 process_user_data:")
    users = [
        {'id': 1, 'name': 'Alice', 'is_active': True},
        {'id': 5, 'name': 'Bob', 'is_active': True},  # 被阻止的用户
        {'id': 10, 'name': 'Charlie', 'is_active': False},
        {'id': 15, 'name': 'David', 'is_active': True},  # 被阻止的用户
    ]
    active = process_user_data(users)
    print(f"   活跃用户数: {len(active)}")
    print(f"   活跃用户: {[u['name'] for u in active]}")
    
    # 测试 parse_config
    print("\n4. 测试 parse_config:")
    config_str = "host=localhost;port=8080;debug=true"
    print(f"   解析结果: {parse_config(config_str)}")
    # print(parse_config(""))  # 取消注释会出错
    # print(parse_config("invalid"))  # 取消注释会出错
    
    # 测试 merge_dicts
    print("\n5. 测试 merge_dicts:")
    original1 = {'a': 1, 'b': 2}
    original2 = {'b': 3, 'c': 4}
    merged = merge_dicts(original1, original2)
    print(f"   合并结果: {merged}")
    print(f"   original1 是否被修改: {original1}")  # 检查是否有副作用
    
    print("\n=== 练习结束 ===")
    print("请找出并修复上述所有问题！")
