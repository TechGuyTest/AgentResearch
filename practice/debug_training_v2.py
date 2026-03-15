#!/usr/bin/env python3
"""
调试训练练习文件 v2
包含多个故意引入的问题，用于调试和代码审查训练

⚠️  警告：此文件包含故意的问题，不要在生产环境中使用！
"""

from typing import List, Dict, Optional
from datetime import datetime


# ============================================================
# 问题 1: 可变默认参数 (Mutable Default Argument)
# ============================================================
# 🐛 提示：默认参数在函数定义时只计算一次
def add_user_to_list(username: str, user_list: list = []) -> list:
    """
    将用户添加到用户列表中
    
    Args:
        username: 用户名
        user_list: 用户列表
    
    Returns:
        更新后的用户列表
    """
    user_list.append(username)
    return user_list


# ============================================================
# 问题 2: 边界情况未处理 (Unprocessed Edge Cases)
# ============================================================
# 🐛 提示：考虑空列表、None 值、负数索引等情况
def get_average_score(scores: List[int]) -> float:
    """
    计算平均分
    
    Args:
        scores: 分数列表
    
    Returns:
        平均分数
    """
    total = sum(scores)
    return total / len(scores)


# ============================================================
# 问题 3: 低效的列表操作 (Inefficient List Operations)
# ============================================================
# 🐛 提示：在循环中使用 list  concatenation 而不是 extend 或列表推导式
def merge_unique_items(lists: List[List[int]]) -> List[int]:
    """
    合并多个列表并去重
    
    Args:
        lists: 多个整数列表
    
    Returns:
        去重后的合并列表
    """
    result = []
    for lst in lists:
        for item in lst:
            if item not in result:  # O(n) 查找，整体 O(n²)
                result = result + [item]  # 每次创建新列表，低效
    return result


# ============================================================
# 问题 4: 逻辑错误 - 错误的条件判断 (Logic Error - Wrong Condition)
# ============================================================
# 🐛 提示：检查条件判断是否正确，特别是 >= 和 > 的区别
def calculate_discount(price: float, quantity: int) -> float:
    """
    根据数量计算折扣后的价格
    
    规则：
    - 数量 >= 10: 9 折
    - 数量 >= 50: 8 折
    - 数量 >= 100: 7 折
    
    Args:
        price: 单价
        quantity: 数量
    
    Returns:
        折扣后的总价
    """
    total = price * quantity
    
    if quantity > 100:  # 🐛 应该是 >= 100
        return total * 0.7
    elif quantity > 50:  # 🐛 应该是 >= 50
        return total * 0.8
    elif quantity > 10:  # 🐛 应该是 >= 10
        return total * 0.9
    else:
        return total


# ============================================================
# 问题 5: 异常处理不当 (Improper Exception Handling)
# ============================================================
# 🐛 提示：过于宽泛的异常捕获，隐藏了真正的错误
def parse_user_data(data: Dict) -> Optional[Dict]:
    """
    解析用户数据
    
    Args:
        data: 原始数据字典
    
    Returns:
        解析后的用户数据，失败返回 None
    """
    try:
        user = {
            "id": data["user_id"],
            "name": data["username"].strip(),
            "age": int(data["age"]),
            "email": data["email"].lower(),
            "created_at": datetime.fromisoformat(data["created"])
        }
        return user
    except Exception:  # 🐛 捕获所有异常，难以调试
        return None


# ============================================================
# 问题 6: 资源泄漏风险 (Resource Leak Risk)
# ============================================================
# 🐛 提示：文件操作没有正确使用上下文管理器
def read_config_file(filepath: str) -> Dict:
    """
    读取配置文件
    
    Args:
        filepath: 配置文件路径
    
    Returns:
        配置字典
    """
    import json
    f = open(filepath, 'r')  # 🐛 没有使用 with 语句
    content = f.read()
    # 🐛 如果 json.loads 抛出异常，文件不会关闭
    config = json.loads(content)
    f.close()
    return config


# ============================================================
# 问题 7: 字符串比较错误 (String Comparison Error)
# ============================================================
# 🐛 提示：检查字符串比较是否正确
def validate_status(status: str) -> bool:
    """
    验证状态是否有效
    
    Args:
        status: 状态字符串
    
    Returns:
        是否有效
    """
    valid_statuses = ["active", "inactive", "pending"]
    return status in valid_statuses or status == "Active"  # 🐛 大小写不一致


# ============================================================
# 测试代码 (包含会暴露问题的测试用例)
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("调试训练练习 - 测试用例")
    print("=" * 60)
    
    # 测试问题 1: 可变默认参数
    print("\n[测试 1] 可变默认参数")
    list1 = add_user_to_list("alice")
    list2 = add_user_to_list("bob")
    print(f"list1: {list1}")
    print(f"list2: {list2}")
    print(f"问题：list2 是否包含了 alice? {('alice' in list2)}")
    
    # 测试问题 2: 边界情况
    print("\n[测试 2] 边界情况 - 空列表")
    try:
        avg = get_average_score([])
        print(f"平均分：{avg}")
    except Exception as e:
        print(f"错误：{type(e).__name__}: {e}")
    
    # 测试问题 3: 低效操作
    print("\n[测试 3] 合并去重")
    lists = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    result = merge_unique_items(lists)
    print(f"合并结果：{result}")
    
    # 测试问题 4: 折扣计算
    print("\n[测试 4] 折扣计算边界")
    print(f"数量=10: {calculate_discount(100, 10)} (期望：900)")
    print(f"数量=50: {calculate_discount(100, 50)} (期望：4000)")
    print(f"数量=100: {calculate_discount(100, 100)} (期望：7000)")
    
    # 测试问题 5: 异常处理
    print("\n[测试 5] 异常处理")
    bad_data = {"user_id": 1, "username": " test ", "age": "invalid", "email": "TEST@EXAMPLE.COM", "created": "2024-01-01"}
    result = parse_user_data(bad_data)
    print(f"解析结果：{result}")
    print("问题：无法知道具体是哪个字段出错")
    
    # 测试问题 7: 字符串比较
    print("\n[测试 7] 字符串比较")
    print(f"'active' 有效：{validate_status('active')}")
    print(f"'Active' 有效：{validate_status('Active')}")
    print(f"'ACTIVE' 有效：{validate_status('ACTIVE')}")
    
    print("\n" + "=" * 60)
    print("练习结束 - 请找出并修复所有问题!")
    print("=" * 60)
