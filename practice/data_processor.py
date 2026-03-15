"""
数据处理器练习文件
此文件包含多个故意的问题，用于调试和代码审查训练。
每个问题都用 TODO 注释标记，请尝试找出并修复它们。
"""

from typing import List, Dict, Optional


def calculate_average(numbers: List[float]) -> float:
    """
    计算数字列表的平均值
    
    TODO: 问题 1 - 边界情况未处理
    提示：当列表为空时会发生什么？
    """
    total = sum(numbers)
    return total / len(numbers)


def find_maximum(values: List[int]) -> int:
    """
    找到列表中的最大值
    
    TODO: 问题 2 - 逻辑错误
    提示：初始值设置是否正确？考虑所有负数的情况。
    """
    max_value = 0  # 这里有问题
    for value in values:
        if value > max_value:
            max_value = value
    return max_value


def process_user_data(users: List[Dict]) -> List[Dict]:
    """
    处理用户数据，添加年龄组分类
    
    TODO: 问题 3 - 类型检查缺失和键访问错误
    提示：如果用户字典中没有 'age' 键会怎样？
    提示：如果 age 不是数字类型会怎样？
    """
    result = []
    for user in users:
        age = user['age']
        if age < 18:
            group = 'minor'
        elif age < 60:
            group = 'adult'
        else:
            group = 'senior'
        
        user['age_group'] = group
        result.append(user)
    return result


def search_items(items: List[str], target: str) -> List[int]:
    """
    搜索列表中所有匹配项的索引
    
    TODO: 问题 4 - 低效模式
    提示：这个实现的时间复杂度是多少？有没有更高效的方法？
    提示：注意字符串比较的方式。
    """
    indices = []
    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == target and i == j:
                indices.append(i)
    return indices


def merge_data(data1: Optional[List], data2: Optional[List]) -> List:
    """
    合并两个数据列表
    
    TODO: 问题 5 - 可变默认参数和 None 处理
    提示：如果两个参数都是 None 会怎样？
    提示：这个函数有默认参数吗？有的话有什么问题？
    """
    # 注意：这个函数设计有缺陷
    result = data1 if data1 else []
    result.extend(data2 if data2 else [])
    return result


def validate_email(email: str) -> bool:
    """
    简单的邮箱验证
    
    TODO: 问题 6 - 不完整的验证逻辑
    提示：这个验证足够吗？考虑 edge cases。
    """
    if '@' in email and '.' in email:
        return True
    return False


# 测试代码
if __name__ == "__main__":
    # 测试 calculate_average
    print("测试平均值计算:")
    print(calculate_average([1, 2, 3, 4, 5]))
    # print(calculate_average([]))  # 取消注释会看到问题
    
    # 测试 find_maximum
    print("\n测试查找最大值:")
    print(find_maximum([1, 5, 3, 9, 2]))
    print(find_maximum([-5, -2, -10, -1]))  # 这个会返回错误结果
    
    # 测试 process_user_data
    print("\n测试用户数据处理:")
    users = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 17},
        {'name': 'Charlie', 'age': 65},
    ]
    print(process_user_data(users))
    
    # 测试 search_items
    print("\n测试搜索项目:")
    items = ['apple', 'banana', 'apple', 'orange', 'apple']
    print(search_items(items, 'apple'))
    
    # 测试 merge_data
    print("\n测试数据合并:")
    print(merge_data([1, 2], [3, 4]))
    print(merge_data(None, [5, 6]))
    
    # 测试 validate_email
    print("\n测试邮箱验证:")
    print(validate_email("test@example.com"))
    print(validate_email("invalid"))
    print(validate_email("@."))  # 这个会错误地返回 True
