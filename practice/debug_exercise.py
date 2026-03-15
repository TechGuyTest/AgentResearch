"""
调试练习文件 - Debug Practice Exercise
=====================================
这个文件包含多个故意引入的问题，用于调试和代码审查训练。
请找出并修复所有问题。

提示：问题类型包括逻辑错误、边界情况、低效模式、异常处理等。
"""


def calculate_average(numbers):
    """
    计算数字列表的平均值
    
    ⚠️ 问题提示：边界情况处理
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_maximum(items):
    """
    找到列表中的最大值
    
    ⚠️ 问题提示：逻辑错误
    """
    if not items:
        return None
    
    max_value = 0  # 问题：如果所有值都是负数怎么办？
    for item in items:
        if item > max_value:
            max_value = item
    return max_value


def process_user_data(users):
    """
    处理用户数据，提取活跃用户
    
    ⚠️ 问题提示：低效模式和潜在错误
    """
    active_users = []
    
    # 问题：多次遍历列表，效率低下
    for user in users:
        if user.get('status') == 'active':
            active_users.append(user)
    
    # 问题：再次遍历，可以合并到上面的循环
    result = []
    for user in active_users:
        if user.get('age', 0) >= 18:
            result.append(user)
    
    # 问题：再次遍历进行数据转换
    final_result = []
    for user in result:
        final_result.append({
            'name': user.get('name'),
            'email': user.get('email'),
            'age': user.get('age')
        })
    
    return final_result


def read_file_safely(filename):
    """
    安全地读取文件内容
    
    ⚠️ 问题提示：异常处理不完整
    """
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content


def search_in_list(data_list, target):
    """
    在列表中搜索目标值，返回索引
    
    ⚠️ 问题提示：边界情况和返回值问题
    """
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    # 问题：没有找到时返回什么？


def merge_dicts(dict1, dict2):
    """
    合并两个字典
    
    ⚠️ 问题提示：副作用和可变参数
    """
    # 问题：直接修改了传入的 dict1，可能产生意外副作用
    for key, value in dict2.items():
        dict1[key] = value
    return dict1


def validate_email(email):
    """
    验证邮箱格式
    
    ⚠️ 问题提示：验证逻辑不完整
    """
    # 问题：非常不完整的邮箱验证
    if '@' in email:
        return True
    return False


# ============================================
# 测试代码
# ============================================
if __name__ == "__main__":
    # 测试 calculate_average
    print("测试 calculate_average:")
    print(calculate_average([1, 2, 3, 4, 5]))  # 应该输出 3.0
    # print(calculate_average([]))  # 会发生什么？
    
    # 测试 find_maximum
    print("\n测试 find_maximum:")
    print(find_maximum([1, 5, 3, 9, 2]))  # 应该输出 9
    print(find_maximum([-5, -2, -10, -1]))  # 会输出什么？正确吗？
    
    # 测试 process_user_data
    print("\n测试 process_user_data:")
    users = [
        {'name': 'Alice', 'status': 'active', 'age': 25, 'email': 'alice@example.com'},
        {'name': 'Bob', 'status': 'inactive', 'age': 30, 'email': 'bob@example.com'},
        {'name': 'Charlie', 'status': 'active', 'age': 17, 'email': 'charlie@example.com'},
    ]
    print(process_user_data(users))
    
    # 测试 search_in_list
    print("\n测试 search_in_list:")
    print(search_in_list([1, 2, 3, 4, 5], 3))  # 应该输出 2
    print(search_in_list([1, 2, 3], 10))  # 会输出什么？
    
    # 测试 merge_dicts
    print("\n测试 merge_dicts:")
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    print(merge_dicts(d1, d2))
    print(f"原始 d1 被修改了吗？{d1}")
    
    # 测试 validate_email
    print("\n测试 validate_email:")
    print(validate_email("test@example.com"))  # True
    print(validate_email("invalid"))  # False
    print(validate_email("@"))  # 会输出什么？合理吗？
    print(validate_email("user@"))  # 会输出什么？合理吗？
