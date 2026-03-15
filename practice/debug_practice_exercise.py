"""
调试练习文件 - Debug Practice Exercise

这个文件包含多个故意引入的问题，用于调试训练。
请找出并修复所有问题。

问题类型：逻辑错误、边界情况未处理、低效模式、可变默认参数等
"""


# ============================================================
# 问题 1: 可变默认参数陷阱
# 提示：默认参数在函数定义时只计算一次
# ============================================================
def add_item_to_list(item, item_list=[]):
    """
    将项目添加到列表中并返回列表。
    
    预期行为：每次调用都应该返回只包含新项目的新列表
    实际行为：？？？
    """
    item_list.append(item)
    return item_list


# ============================================================
# 问题 2: 边界情况未处理 - 除零错误
# 提示：当 divisor 为 0 时会发生什么？
# ============================================================
def calculate_average(numbers):
    """
    计算数字列表的平均值。
    
    参数:
        numbers: 数字列表
    
    返回:
        平均值（浮点数）
    
    问题：如果列表为空会发生什么？
    """
    total = sum(numbers)
    count = len(numbers)
    return total / count


# ============================================================
# 问题 3: 低效的列表查找模式
# 提示：在循环中使用 'in' 操作符检查列表成员的复杂度是多少？
# 整体时间复杂度是多少？有更高的方法吗？
# ============================================================
def find_duplicates(numbers):
    """
    找出列表中所有重复的数字。
    
    参数:
        numbers: 整数列表
    
    返回:
        包含所有重复数字的列表（每个重复数字只出现一次）
    
    问题：这个实现的时间复杂度是多少？如何优化？
    """
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates


# ============================================================
# 问题 4: 逻辑错误 - 条件判断错误
# 提示：仔细检查条件判断的逻辑
# ============================================================
def is_valid_age(age):
    """
    检查年龄是否有效（0-150 之间）。
    
    参数:
        age: 年龄（整数）
    
    返回:
        如果年龄有效返回 True，否则返回 False
    
    问题：这个函数能正确处理所有边界情况吗？
    """
    if age > 0 or age < 150:
        return True
    return False


# ============================================================
# 问题 5: 文件资源未正确关闭
# 提示：如果读取过程中发生异常会发生什么？
# ============================================================
def read_file_content(filepath):
    """
    读取文件内容并返回行列表。
    
    参数:
        filepath: 文件路径
    
    返回:
        包含文件所有行的列表
    
    问题：文件是否总是被正确关闭？
    """
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    return lines


# ============================================================
# 问题 6: 字符串比较错误
# 提示：如何正确比较字符串内容？
# ============================================================
def find_user_by_name(users, target_name):
    """
    在用户列表中查找指定名称的用户。
    
    参数:
        users: 用户字典列表，每个字典包含 'name' 和 'id' 键
        target_name: 要查找的用户名
    
    返回:
        匹配的用户字典，如果未找到则返回 None
    
    问题：字符串比较是否正确？
    """
    for user in users:
        if user['name'] is target_name:
            return user
    return None


# ============================================================
# 问题 7: 浮点数比较问题
# 提示：直接比较浮点数相等有什么问题？
# ============================================================
def is_close_to_zero(value):
    """
    检查一个值是否接近零。
    
    参数:
        value: 浮点数
    
    返回:
        如果值在 -0.0001 到 0.0001 之间返回 True
    
    问题：这个比较方式有什么问题？
    """
    return value == 0.0


# ============================================================
# 测试代码 - 用于验证问题
# ============================================================
if __name__ == "__main__":
    print("=== 调试练习测试 ===\n")
    
    # 测试问题 1
    print("测试 1: 可变默认参数")
    result1 = add_item_to_list(1)
    result2 = add_item_to_list(2)
    print(f"第一次调用结果：{result1}")
    print(f"第二次调用结果：{result2}")
    print(f"预期：[1] 和 [2]，实际是否相同？{result1 is result2}\n")
    
    # 测试问题 2
    print("测试 2: 空列表平均值")
    try:
        avg = calculate_average([])
        print(f"空列表平均值：{avg}")
    except Exception as e:
        print(f"错误：{type(e).__name__}: {e}\n")
    
    # 测试问题 3
    print("测试 3: 查找重复项")
    test_list = [1, 2, 3, 2, 4, 3, 5]
    dups = find_duplicates(test_list)
    print(f"输入：{test_list}")
    print(f"重复项：{dups}")
    print(f"预期：[2, 3]\n")
    
    # 测试问题 4
    print("测试 4: 年龄验证")
    print(f"is_valid_age(25) = {is_valid_age(25)} (预期：True)")
    print(f"is_valid_age(0) = {is_valid_age(0)} (预期：False)")
    print(f"is_valid_age(200) = {is_valid_age(200)} (预期：False)")
    print(f"is_valid_age(-5) = {is_valid_age(-5)} (预期：False)\n")
    
    # 测试问题 6
    print("测试 6: 字符串比较")
    users = [{'name': 'Alice', 'id': 1}, {'name': 'Bob', 'id': 2}]
    target = 'Alice'
    found = find_user_by_name(users, target)
    print(f"查找 '{target}': {found}")
    print(f"预期：{{'name': 'Alice', 'id': 1}}\n")
    
    # 测试问题 7
    print("测试 7: 浮点数比较")
    print(f"is_close_to_zero(0.0) = {is_close_to_zero(0.0)}")
    print(f"is_close_to_zero(0.00001) = {is_close_to_zero(0.00001)}")
    print(f"is_close_to_zero(1e-10) = {is_close_to_zero(1e-10)}")
    print("预期：0.00001 和 1e-10 也应该被认为是接近零的\n")
    
    print("=== 测试结束 ===")
