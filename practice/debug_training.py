#!/usr/bin/env python3
"""
调试训练练习文件
本文件包含多个故意引入的问题，用于调试和代码审查训练。
请找出并修复所有问题。

问题类型：逻辑错误、边界情况未处理、低效模式、异常处理缺失等
"""

# ============================================================
# 问题 1: 边界情况未处理 - 空列表和 None 值
# ============================================================
def calculate_average(numbers):
    """
    计算数字列表的平均值
    
    ⚠️ 提示：考虑空列表的情况会发生什么？
    ⚠️ 提示：如果传入 None 会怎样？
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


# ============================================================
# 问题 2: 逻辑错误 - 条件判断错误
# ============================================================
def is_valid_age(age):
    """
    检查年龄是否有效（0-150 岁之间）
    
    ⚠️ 提示：检查条件判断逻辑是否正确
    ⚠️ 提示：边界值 0 和 150 是否被正确处理？
    """
    if age > 0 or age < 150:
        return True
    return False


# ============================================================
# 问题 3: 低效模式 - 不必要的重复计算
# ============================================================
def find_duplicates(items):
    """
    找出列表中的重复项
    
    ⚠️ 提示：这个实现的时间复杂度是多少？
    ⚠️ 提示：是否有更高效的方法？
    ⚠️ 提示：注意列表在循环中被修改的问题
    """
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates


# ============================================================
# 问题 4: 异常处理缺失 - 文件操作
# ============================================================
def read_config_file(filepath):
    """
    读取配置文件并解析为字典
    
    ⚠️ 提示：如果文件不存在会怎样？
    ⚠️ 提示：如果文件格式不正确会怎样？
    ⚠️ 提示：文件是否被正确关闭？
    """
    file = open(filepath, 'r')
    content = file.read()
    config = {}
    for line in content.split('\n'):
        key, value = line.split('=')
        config[key.strip()] = value.strip()
    return config


# ============================================================
# 问题 5: 可变默认参数陷阱
# ============================================================
def add_item_to_inventory(item, inventory=[]):
    """
    将物品添加到库存列表
    
    ⚠️ 提示：多次调用此函数会发生什么？
    ⚠️ 提示：默认参数在 Python 中是如何工作的？
    """
    inventory.append(item)
    return inventory


# ============================================================
# 问题 6: 字符串比较错误
# ============================================================
def check_user_role(user_role, required_role):
    """
    检查用户角色是否符合要求
    
    ⚠️ 提示：字符串比较是否考虑了大小写？
    ⚠️ 提示：如果 user_role 是 None 会怎样？
    """
    if user_role == required_role:
        return True
    return False


# ============================================================
# 问题 7: 浮点数比较问题
# ============================================================
def is_price_equal(price1, price2):
    """
    检查两个价格是否相等
    
    ⚠️ 提示：直接使用 == 比较浮点数有什么问题？
    ⚠️ 提示：考虑浮点数精度问题
    """
    return price1 == price2


# ============================================================
# 测试代码（也包含问题）
# ============================================================
if __name__ == "__main__":
    # 测试 calculate_average
    print("测试平均值计算:")
    print(calculate_average([1, 2, 3, 4, 5]))  # 应该输出 3.0
    # print(calculate_average([]))  # 会发生什么？
    
    # 测试 is_valid_age
    print("\n测试年龄验证:")
    print(f"age=25: {is_valid_age(25)}")  # 应该 True
    print(f"age=0: {is_valid_age(0)}")    # 应该 False，但实际呢？
    print(f"age=150: {is_valid_age(150)}") # 应该 True，但实际呢？
    
    # 测试 find_duplicates
    print("\n测试查找重复项:")
    print(find_duplicates([1, 2, 2, 3, 3, 3]))  # 应该输出 [2, 3]
    
    # 测试 add_item_to_inventory
    print("\n测试库存添加:")
    print(add_item_to_inventory("apple"))
    print(add_item_to_inventory("banana"))  # 会发生什么？
    
    # 测试浮点数比较
    print("\n测试价格比较:")
    print(is_price_equal(0.1 + 0.2, 0.3))  # 会输出 True 吗？
