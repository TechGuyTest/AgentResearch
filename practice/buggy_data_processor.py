"""
数据处理器练习文件 - 包含多个需要修复的问题

这个文件故意包含了一些常见的编程错误和低效模式，
用于调试和代码审查训练。

请找出并修复所有问题。
"""

import json
from datetime import datetime
from typing import List, Dict, Any


# 问题 1: 可变默认参数陷阱
# 提示：默认参数在函数定义时只计算一次
def add_user_to_list(username: str, user_list: list = []) -> list:
    """添加用户到用户列表"""
    user_list.append(username)
    return user_list


# 问题 2: 边界情况未处理 - 除零错误
# 提示：当 total 为 0 时会发生什么？
def calculate_average(scores: List[float]) -> float:
    """计算平均分"""
    total = sum(scores)
    return total / len(scores)


# 问题 3: 低效的列表查找模式
# 提示：在循环中重复查找，时间复杂度 O(n²)
def find_duplicates(items: List[Any]) -> List[Any]:
    """找出列表中的重复项"""
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates


# 问题 4: 逻辑错误 - 条件判断不正确
# 提示：检查年龄验证的逻辑是否正确
def is_eligible_for_discount(age: int, is_member: bool) -> bool:
    """
    检查是否符合折扣条件：
    - 会员 always 符合
    - 非会员年龄 >= 65 或 <= 18 符合
    """
    if is_member or age > 65 and age < 18:
        return True
    return False


# 问题 5: 资源未正确关闭
# 提示：文件操作后没有正确关闭
def load_config(config_path: str) -> Dict:
    """加载配置文件"""
    config_file = open(config_path, 'r')
    config = json.load(config_file)
    # 缺少关闭文件的操作
    return config


# 问题 6: 字符串拼接低效
# 提示：在循环中使用 += 拼接字符串效率低下
def build_message(items: List[str]) -> str:
    """构建消息字符串"""
    message = ""
    for i, item in enumerate(items):
        message += f"Item {i}: {item}\n"
    return message


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


# 问题 10: 不正确的类型比较
# 提示：检查类型比较是否正确
def validate_input(value: Any) -> bool:
    """验证输入是否为有效数字"""
    if type(value) == int or type(value) == float:
        return True
    return False


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
