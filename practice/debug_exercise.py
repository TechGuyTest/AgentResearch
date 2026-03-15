"""
调试练习文件 - Debug Exercise
============================
这个文件包含多个故意引入的问题，用于调试和代码审查训练。
请找出并修复所有问题。

问题类型：逻辑错误、边界情况、低效模式、资源管理等
"""


# ============================================================
# 问题 1: 可变默认参数陷阱 (Mutable Default Argument)
# ============================================================
# 提示：默认参数在函数定义时只计算一次
def add_item(item, items=[]):
    """
    将项目添加到列表中。
    
    问题：使用可变对象作为默认参数
    """
    items.append(item)
    return items


# ============================================================
# 问题 2: 边界情况未处理 (Unprocessed Edge Cases)
# ============================================================
# 提示：考虑除零、空列表、负数等情况
def calculate_average(numbers):
    """
    计算数字列表的平均值。
    
    问题：未处理空列表和除零情况
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


# ============================================================
# 问题 3: 低效的循环模式 (Inefficient Loop Pattern)
# ============================================================
# 提示：在循环中重复计算不变的值
def find_duplicates(data_list):
    """
    找出列表中的重复元素。
    
    问题：时间复杂度 O(n²)，可以优化到 O(n)
    """
    duplicates = []
    for i in range(len(data_list)):
        for j in range(len(data_list)):
            if i != j and data_list[i] == data_list[j]:
                if data_list[i] not in duplicates:
                    duplicates.append(data_list[i])
    return duplicates


# ============================================================
# 问题 4: 逻辑错误 - 错误的条件判断 (Logic Error)
# ============================================================
# 提示：检查条件判断的逻辑运算符
def is_valid_age(age):
    """
    检查年龄是否在有效范围内 (0-150)。
    
    问题：使用了错误的逻辑运算符
    """
    # 应该是 age >= 0 AND age <= 150
    if age >= 0 or age <= 150:
        return True
    return False


# ============================================================
# 问题 5: 资源未正确关闭 (Resource Not Properly Closed)
# ============================================================
# 提示：文件操作后需要确保关闭
def read_file_content(filepath):
    """
    读取文件内容。
    
    问题：文件打开后未正确关闭，异常情况下会泄露资源
    """
    file = open(filepath, 'r')
    content = file.read()
    # 如果 read() 抛出异常，文件将不会关闭
    file.close()
    return content


# ============================================================
# 问题 6: 字符串比较错误 (String Comparison Error)
# ============================================================
# 提示：检查字符串比较的方式
def check_user_input(user_input):
    """
    检查用户输入是否为 'yes'。
    
    问题：大小写敏感，且未处理 None 情况
    """
    if user_input == 'yes':
        return True
    return False


# ============================================================
# 测试代码
# ============================================================
if __name__ == "__main__":
    print("=== 调试练习测试 ===\n")
    
    # 测试问题 1
    print("1. 测试可变默认参数:")
    print(f"   第一次调用: {add_item(1)}")
    print(f"   第二次调用: {add_item(2)}")
    print(f"   预期：[1], [2] | 实际如上\n")
    
    # 测试问题 2
    print("2. 测试边界情况:")
    try:
        result = calculate_average([])
        print(f"   空列表平均值: {result}")
    except Exception as e:
        print(f"   空列表导致错误: {e}\n")
    
    # 测试问题 3
    print("3. 测试重复查找:")
    test_data = [1, 2, 3, 2, 4, 3, 5]
    print(f"   输入: {test_data}")
    print(f"   重复元素: {find_duplicates(test_data)}\n")
    
    # 测试问题 4
    print("4. 测试年龄验证:")
    print(f"   age=-5 有效吗？{is_valid_age(-5)} (预期: False)")
    print(f"   age=200 有效吗？{is_valid_age(200)} (预期: False)\n")
    
    # 测试问题 5
    print("5. 测试文件读取:")
    print("   (需要实际文件测试)\n")
    
    # 测试问题 6
    print("6. 测试用户输入:")
    print(f"   'YES' 有效吗？{check_user_input('YES')} (预期: True)")
    print(f"   'Yes' 有效吗？{check_user_input('Yes')} (预期: True)")
    print(f"   None 有效吗？{check_user_input(None)} (预期: False)\n")
