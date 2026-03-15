#!/usr/bin/env python3
"""
Debug Training Exercise V7
这个文件包含多个故意的问题，用于调试训练练习。
请找出并修复所有问题。

问题类型：逻辑错误、边界情况、低效模式、类型安全、资源管理
"""


# ============================================================
# 问题 1: 逻辑错误 - 条件判断有误
# 提示：检查温度分类的边界条件
# ============================================================
def classify_temperature(celsius):
    """
    根据摄氏温度返回分类：
    - "freezing": <= 0
    - "cold": 1-15
    - "moderate": 16-25
    - "hot": 26-35
    - "extreme": > 35
    """
    # BUG: 条件判断有重叠和遗漏
    if celsius < 0:
        return "freezing"
    elif celsius <= 15:
        return "cold"
    elif celsius <= 25:
        return "moderate"
    elif celsius <= 35:
        return "hot"
    else:
        return "extreme"


# ============================================================
# 问题 2: 边界情况未处理 - 空列表和 None 值
# 提示：当输入为空或包含 None 时会发生什么？
# ============================================================
def calculate_average(numbers):
    """
    计算数字列表的平均值
    """
    # BUG: 没有处理空列表的情况
    # BUG: 没有处理列表中包含 None 的情况
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


# ============================================================
# 问题 3: 低效模式 - 重复计算和不必要的循环
# 提示：这个函数可以优化吗？
# ============================================================
def find_duplicates(items):
    """
    找出列表中的重复项
    返回一个包含所有重复项的列表
    """
    duplicates = []
    # BUG: O(n²) 复杂度，可以优化
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates


# ============================================================
# 问题 4: 类型安全风险 - 未进行输入验证
# 提示：如果传入错误的类型会怎样？
# ============================================================
def process_user_data(user_id, username, age):
    """
    处理用户数据并返回格式化的字符串
    """
    # BUG: 没有类型检查，如果 age 是字符串会出错
    # BUG: 没有验证 user_id 是否为正数
    # BUG: 没有验证 age 的合理范围
    
    if age > 18:
        status = "adult"
    else:
        status = "minor"
    
    return f"User {user_id}: {username} ({age} years old, {status})"


# ============================================================
# 问题 5: 资源泄漏 - 文件未正确关闭
# 提示：如果读取过程中发生异常会怎样？
# ============================================================
def read_config_file(filepath):
    """
    读取配置文件并返回内容
    """
    # BUG: 文件打开后没有确保关闭
    # BUG: 没有处理文件不存在的情况
    # BUG: 没有处理编码问题
    file = open(filepath, 'r')
    content = file.read()
    file.close()
    return content


# ============================================================
# 问题 6: 字符串处理错误 - 可变默认参数
# 提示：默认参数是可变对象时会有什么问题？
# ============================================================
def build_message(items, prefix="Welcome: ", cache=[]):
    """
    构建消息字符串，使用缓存避免重复处理
    """
    # BUG: 可变默认参数 cache 会在多次调用间共享
    for item in items:
        if item not in cache:
            cache.append(item)
    
    return prefix + ", ".join(cache)


# ============================================================
# 测试代码
# ============================================================
if __name__ == "__main__":
    print("=== Debug Training Exercise V7 ===\n")
    
    # 测试温度分类
    print("1. 温度分类测试:")
    test_temps = [-5, 0, 10, 15, 20, 25, 30, 35, 40]
    for temp in test_temps:
        print(f"   {temp}°C -> {classify_temperature(temp)}")
    
    # 测试平均值计算
    print("\n2. 平均值计算测试:")
    try:
        print(f"   [1, 2, 3, 4, 5] 的平均值: {calculate_average([1, 2, 3, 4, 5])}")
        # print(f"   空列表的平均值: {calculate_average([])}")  # 会出错
    except Exception as e:
        print(f"   错误: {e}")
    
    # 测试重复项查找
    print("\n3. 重复项查找测试:")
    test_items = [1, 2, 3, 2, 4, 3, 5, 1]
    print(f"   {test_items} 中的重复项: {find_duplicates(test_items)}")
    
    # 测试用户数据处理
    print("\n4. 用户数据处理测试:")
    try:
        print(f"   {process_user_data(1, 'Alice', 25)}")
        # print(f"   {process_user_data(2, 'Bob', 'twenty')}")  # 类型错误
    except Exception as e:
        print(f"   错误: {e}")
    
    # 测试消息构建
    print("\n5. 消息构建测试:")
    print(f"   第一次调用: {build_message(['A', 'B'])}")
    print(f"   第二次调用: {build_message(['C', 'D'])}")  # 会包含第一次的数据
    
    print("\n=== 练习结束 ===")
    print("请找出并修复上述代码中的所有问题！")
