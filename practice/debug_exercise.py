"""
调试练习文件 - Debug Practice Exercise
包含多个故意的问题用于调试训练
Contains intentional bugs for debugging practice
"""

# ============================================
# 问题 1: 边界情况未处理 (Boundary case not handled)
# 当 numbers 为空列表时会发生什么？
# What happens when numbers is an empty list?
# ============================================
def calculate_average(numbers):
    """计算列表的平均值"""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


# ============================================
# 问题 2: 逻辑错误 (Logic error)
# 这个函数应该返回最大值，但有什么错误？
# This function should return the maximum value, but what's wrong?
# ============================================
def find_maximum(numbers):
    """找到列表中的最大值"""
    if not numbers:
        return None
    
    max_value = 0  # 提示：这里有什么问题？
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


# ============================================
# 问题 3: 低效模式 (Inefficient pattern)
# 这个函数有什么性能问题？如何优化？
# What performance issue does this function have? How to optimize?
# ============================================
def search_item(items, target):
    """在列表中搜索目标项"""
    found_items = []
    for i in range(len(items)):
        if items[i] == target:
            # 提示：每次迭代都重新创建列表是否高效？
            found_items = []  # 这里有什么问题？
            found_items.append(i)
    return found_items


# ============================================
# 问题 4: 可变默认参数 (Mutable default argument)
# 这个函数多次调用会有什么问题？
# What problem occurs when calling this function multiple times?
# ============================================
def add_user_to_list(username, user_list=[]):
    """将用户添加到列表中"""
    # 提示：使用可变对象作为默认参数安全吗？
    user_list.append(username)
    return user_list


# ============================================
# 问题 5: 异常处理不当 (Improper exception handling)
# 这个函数的异常处理有什么问题？
# What's wrong with the exception handling in this function?
# ============================================
def read_config_file(filepath):
    """读取配置文件"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            return content
    except Exception:
        # 提示：捕获所有异常但不做任何处理是否合适？
        pass
    
    return None


# ============================================
# 问题 6: 类型比较问题 (Type comparison issue)
# 这个函数在比较时有什么潜在问题？
# What potential issue exists in the comparison?
# ============================================
def check_user_access(user_input, required_level):
    """检查用户访问级别"""
    # 提示：直接比较不同类型的值安全吗？
    if user_input == required_level:
        return True
    elif user_input > required_level:
        return True
    return False


# ============================================
# 测试代码
# Test code
# ============================================
if __name__ == "__main__":
    print("=== 调试练习测试 ===")
    print("=== Debug Exercise Test ===\n")
    
    # 测试 calculate_average
    print("1. 测试 calculate_average:")
    try:
        result = calculate_average([1, 2, 3, 4, 5])
        print(f"   average([1,2,3,4,5]) = {result}")
    except Exception as e:
        print(f"   错误：{e}")
    
    # 测试 find_maximum
    print("\n2. 测试 find_maximum:")
    print(f"   maximum([-5, -2, -10]) = {find_maximum([-5, -2, -10])}")
    print(f"   期望值：-2")
    
    # 测试 search_item
    print("\n3. 测试 search_item:")
    items = ['a', 'b', 'c', 'b', 'd', 'b']
    print(f"   search_item({items}, 'b') = {search_item(items, 'b')}")
    print(f"   期望值：[1, 3, 5]")
    
    # 测试 add_user_to_list
    print("\n4. 测试 add_user_to_list:")
    print(f"   第一次调用：{add_user_to_list('Alice')}")
    print(f"   第二次调用：{add_user_to_list('Bob')}")
    print(f"   第三次调用：{add_user_to_list('Charlie')}")
    print(f"   提示：每次调用应该返回独立的用户列表")
    
    # 测试 read_config_file
    print("\n5. 测试 read_config_file:")
    result = read_config_file('/nonexistent/path/config.txt')
    print(f"   读取不存在的文件返回：{result}")
    print(f"   提示：应该有更明确的错误处理")
    
    # 测试 check_user_access
    print("\n6. 测试 check_user_access:")
    print(f"   check_user_access('3', 2) = {check_user_access('3', 2)}")
    print(f"   check_user_access(3, 2) = {check_user_access(3, 2)}")
    print(f"   提示：字符串和整数的比较结果可能不符合预期")
    
    print("\n=== 练习结束 ===")
    print("=== Exercise Complete ===")
