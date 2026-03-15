"""
数据处理器练习文件 - 包含多个需要修复的问题

这个文件故意包含了一些常见的编程错误和低效模式，
用于调试和代码审查训练。

请找出并修复所有问题。
"""

import json
from datetime import datetime
from typing import List, Dict, Any


# 修复 1: 使用 None 作为默认值，避免可变默认参数陷阱
def add_user_to_list(username: str, user_list: list = None) -> list:
    """添加用户到用户列表"""
    if user_list is None:
        user_list = []
    user_list.append(username)
    return user_list


# 修复 2: 处理空列表边界情况
def calculate_average(scores: List[float]) -> float:
    """计算平均分"""
    if not scores:
        raise ValueError("Cannot calculate average of empty list")
    total = sum(scores)
    return total / len(scores)


# 修复 3: 使用集合实现 O(n) 时间复杂度
def find_duplicates(items: List[Any]) -> List[Any]:
    """找出列表中的重复项"""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


# 修复 4: 修正逻辑错误 - 使用 or 而不是 and
def is_eligible_for_discount(age: int, is_member: bool) -> bool:
    """
    检查是否符合折扣条件：
    - 会员 always 符合
    - 非会员年龄 >= 65 或 <= 18 符合
    """
    if is_member or age >= 65 or age <= 18:
        return True
    return False


# 修复 5: 使用上下文管理器确保文件正确关闭
def load_config(config_path: str) -> Dict:
    """加载配置文件"""
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config


# 修复 6: 使用 join 实现高效字符串拼接
def build_message(items: List[str]) -> str:
    """构建消息字符串"""
    messages = [f"Item {i}: {item}\n" for i, item in enumerate(items)]
    return "".join(messages)


# 问题 7: 未处理的异常
# 提示：如果文件不存在或 JSON 格式错误会怎样？
def save_data(data: Dict, filepath: str) -> bool:
    """保存数据到文件"""
    with open(filepath, 'w') as f:
        json.dump(data, f)
    return True


# 问题 8: 时区处理问题
# 提示：直接使用 datetime.now() 可能有时区问题
def get_timestamp() -> str:
    """获取当前时间戳"""
    return datetime.now().isoformat()


# 问题 9: 列表切片创建不必要的副本
# 提示：检查是否真的需要创建新列表
def process_first_half(data: List[int]) -> List[int]:
    """处理列表的前半部分"""
    half = len(data) // 2
    result = data[:half]  # 创建了新副本
    for i in range(len(result)):
        result[i] = result[i] * 2
    return result


# 修复 10: 使用 isinstance 进行正确的类型检查
def validate_input(value: Any) -> bool:
    """验证输入是否为有效数字"""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


# 主函数 - 包含多个调用示例
def main():
    """主函数 - 演示各种功能"""
    print("=== 数据处理器演示 ===\n")
    
    # 测试可变默认参数
    print("测试 1: 添加用户")
    users1 = add_user_to_list("Alice")
    users2 = add_user_to_list("Bob")
    print(f"用户列表 1: {users1}")
    print(f"用户列表 2: {users2}")
    print()
    
    # 测试平均分计算
    print("测试 2: 计算平均分")
    scores = [85, 90, 78, 92]
    print(f"分数: {scores}")
    print(f"平均分: {calculate_average(scores)}")
    print()
    
    # 测试重复项查找
    print("测试 3: 查找重复项")
    items = [1, 2, 3, 2, 4, 1, 5]
    print(f"列表: {items}")
    print(f"重复项: {find_duplicates(items)}")
    print()
    
    # 测试折扣资格
    print("测试 4: 折扣资格检查")
    print(f"会员，年龄 30: {is_eligible_for_discount(30, True)}")
    print(f"非会员，年龄 70: {is_eligible_for_discount(70, False)}")
    print(f"非会员，年龄 15: {is_eligible_for_discount(15, False)}")
    print(f"非会员，年龄 30: {is_eligible_for_discount(30, False)}")
    print()
    
    # 测试消息构建
    print("测试 5: 构建消息")
    items = ["Apple", "Banana", "Cherry"]
    print(build_message(items))
    
    print("=== 演示结束 ===")


if __name__ == "__main__":
    main()
