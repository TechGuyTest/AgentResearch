"""
Debug Training Exercise V5
==========================
这个文件包含多个故意引入的问题，用于调试训练。
请找出并修复所有问题。

提示：寻找逻辑错误、边界情况未处理、低效模式等。
"""


def calculate_average(numbers):
    """
    计算数字列表的平均值
    
    ⚠️ 问题提示：边界情况处理
    """
    total = 0
    for num in numbers:
        total += num
    # TODO: 这里缺少什么检查？
    return total / len(numbers)


def find_maximum(items):
    """
    找到列表中的最大值
    
    ⚠️ 问题提示：逻辑错误
    """
    if not items:
        return None
    
    max_value = 0  # TODO: 这个初始值有什么问题？
    for item in items:
        if item > max_value:
            max_value = item
    return max_value


def process_user_data(users):
    """
    处理用户数据，返回活跃用户列表
    
    ⚠️ 问题提示：低效模式和潜在错误
    """
    active_users = []
    
    # TODO: 这个循环效率如何？可以优化吗？
    for i in range(len(users)):
        user = users[i]
        if user.get('is_active', False):
            # TODO: 这里有什么潜在问题？
            active_users.append({
                'id': user['id'],
                'name': user['name'].upper(),
                'email': user['email']
            })
    
    return active_users


def search_in_list(data_list, target):
    """
    在列表中搜索目标值，返回索引
    
    ⚠️ 问题提示：边界情况和返回值
    """
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    # TODO: 当找不到目标值时，应该返回什么？
    return -1


def merge_dicts(dict1, dict2):
    """
    合并两个字典，dict2 的值覆盖 dict1
    
    ⚠️ 问题提示：副作用问题
    """
    # TODO: 这个实现有什么问题？会修改原始字典吗？
    result = dict1
    for key, value in dict2.items():
        result[key] = value
    return result


def validate_email(email):
    """
    简单的邮箱验证
    
    ⚠️ 问题提示：验证逻辑不完整
    """
    # TODO: 这个验证足够吗？考虑边界情况
    if '@' in email:
        return True
    return False


def calculate_discount(price, discount_percent):
    """
    计算折扣后的价格
    
    ⚠️ 问题提示：边界情况和数据类型
    """
    # TODO: 如果 discount_percent 是负数或超过 100 会怎样？
    # TODO: 如果 price 是字符串会怎样？
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


# ============== 测试代码 ==============
if __name__ == "__main__":
    print("=== Debug Training Exercise V5 ===\n")
    
    # 测试 calculate_average
    print("1. 测试 calculate_average:")
    print(f"   average([1, 2, 3, 4, 5]) = {calculate_average([1, 2, 3, 4, 5])}")
    # print(f"   average([]) = {calculate_average([])}")  # 取消注释会怎样？
    
    # 测试 find_maximum
    print("\n2. 测试 find_maximum:")
    print(f"   maximum([1, 5, 3, 9, 2]) = {find_maximum([1, 5, 3, 9, 2])}")
    print(f"   maximum([-5, -2, -10, -1]) = {find_maximum([-5, -2, -10, -1])}")  # 结果正确吗？
    
    # 测试 process_user_data
    print("\n3. 测试 process_user_data:")
    users = [
        {'id': 1, 'name': 'alice', 'email': 'alice@example.com', 'is_active': True},
        {'id': 2, 'name': 'bob', 'email': 'bob@example.com', 'is_active': False},
        {'id': 3, 'name': 'charlie', 'email': 'charlie@example.com', 'is_active': True},
    ]
    print(f"   active users: {process_user_data(users)}")
    
    # 测试 search_in_list
    print("\n4. 测试 search_in_list:")
    print(f"   search([1, 2, 3, 4, 5], 3) = {search_in_list([1, 2, 3, 4, 5], 3)}")
    print(f"   search([1, 2, 3, 4, 5], 10) = {search_in_list([1, 2, 3, 4, 5], 10)}")
    
    # 测试 merge_dicts
    print("\n5. 测试 merge_dicts:")
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    merged = merge_dicts(d1, d2)
    print(f"   merged: {merged}")
    print(f"   d1 after merge: {d1}")  # d1 被修改了吗？
    
    # 测试 validate_email
    print("\n6. 测试 validate_email:")
    print(f"   validate('test@example.com') = {validate_email('test@example.com')}")
    print(f"   validate('invalid') = {validate_email('invalid')}")
    print(f"   validate('@invalid') = {validate_email('@invalid')}")  # 这应该是有效的吗？
    
    # 测试 calculate_discount
    print("\n7. 测试 calculate_discount:")
    print(f"   discount(100, 20) = {calculate_discount(100, 20)}")
    print(f"   discount(100, 150) = {calculate_discount(100, 150)}")  # 结果合理吗？
    print(f"   discount('100', 20) = {calculate_discount('100', 20)}")  # 会发生什么？
