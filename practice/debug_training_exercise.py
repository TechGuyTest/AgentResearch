"""
Debug Training Exercise - 调试训练练习文件
==========================================
这个文件包含多个故意引入的问题，用于调试和代码审查训练。
请找出并修复所有问题。

问题类型：逻辑错误、边界情况未处理、低效模式、类型安全问题等
"""


# ============================================================
# 问题 1: 逻辑错误 - 平均值计算函数
# TODO: 这个函数在计算平均值时有逻辑错误
# ============================================================
def calculate_average(numbers):
    """
    计算数字列表的平均值
    
    Args:
        numbers: 数字列表
        
    Returns:
        平均值
    """
    # BUG: 这里有问题 - 除数错误
    total = sum(numbers)
    # 提示：当列表为空时会发生什么？除数应该是什么？
    average = total / len(numbers) if numbers else total / 1
    return average


# ============================================================
# 问题 2: 边界情况未处理 - 查找最大值
# TODO: 这个函数没有处理边界情况
# ============================================================
def find_max_value(data_list):
    """
    在列表中查找最大值
    
    Args:
        data_list: 数字列表
        
    Returns:
        最大值
    """
    # BUG: 如果列表为空会发生什么？
    # 提示：考虑空列表、None 值、混合类型等情况
    max_value = data_list[0]
    for item in data_list:
        if item > max_value:
            max_value = item
    return max_value


# ============================================================
# 问题 3: 低效模式 - 重复计算
# TODO: 这个函数有性能问题，存在重复计算
# ============================================================
def process_data(items):
    """
    处理数据列表，返回处理后的结果
    
    Args:
        items: 数据项列表
        
    Returns:
        处理后的字典
    """
    result = {}
    for i in range(len(items)):
        # BUG: 低效 - 每次都重新计算长度
        # 提示：len(items) 在循环中被重复调用
        for j in range(len(items)):
            # BUG: 低效 - 嵌套循环中再次计算长度
            if i != j:
                key = f"{items[i]}_{items[j]}"
                # BUG: 低效 - 每次都重新计算这个值
                value = sum(items) * len(items)
                result[key] = value
    return result


# ============================================================
# 问题 4: 类型安全问题 - 用户数据处理
# TODO: 这个函数没有进行类型检查和验证
# ============================================================
def process_user_data(user_input):
    """
    处理用户输入数据
    
    Args:
        user_input: 用户输入（应该是字典）
        
    Returns:
        处理后的用户数据
    """
    # BUG: 没有类型检查 - 如果 user_input 不是字典会怎样？
    # BUG: 没有验证必需的键是否存在
    name = user_input['name']
    age = user_input['age']
    email = user_input['email']
    
    # BUG: 没有验证 age 是否为有效数字
    # BUG: 没有验证 email 格式
    if age > 18:
        status = "adult"
    else:
        status = "minor"
    
    return {
        'name': name.upper(),
        'age': age,
        'email': email.lower(),
        'status': status
    }


# ============================================================
# 问题 5: 资源泄漏 - 文件操作
# TODO: 这个函数有资源泄漏问题
# ============================================================
def read_and_process_file(filepath):
    """
    读取文件并处理内容
    
    Args:
        filepath: 文件路径
        
    Returns:
        处理后的内容列表
    """
    # BUG: 文件没有正确关闭 - 如果处理过程中出错怎么办？
    # 提示：使用 context manager (with 语句)
    f = open(filepath, 'r')
    content = f.read()
    lines = content.split('\n')
    
    processed = []
    for line in lines:
        # BUG: 如果文件不存在或没有读取权限，上面的代码会抛出异常
        # 且文件不会被关闭
        if line.strip():
            processed.append(line.strip().upper())
    
    # BUG: 只在正常执行时关闭文件，异常时不会关闭
    f.close()
    return processed


# ============================================================
# 主函数 - 用于测试
# ============================================================
if __name__ == "__main__":
    print("=== Debug Training Exercise ===\n")
    
    # 测试问题 1
    print("1. 测试 calculate_average:")
    print(f"   [1, 2, 3, 4, 5] 的平均值: {calculate_average([1, 2, 3, 4, 5])}")
    print(f"   空列表的平均值: {calculate_average([])}")  # 这里会有问题
    print()
    
    # 测试问题 2
    print("2. 测试 find_max_value:")
    print(f"   [3, 1, 4, 1, 5, 9] 的最大值: {find_max_value([3, 1, 4, 1, 5, 9])}")
    # print(f"   空列表的最大值: {find_max_value([])}")  # 取消注释会报错
    print()
    
    # 测试问题 3
    print("3. 测试 process_data (注意性能):")
    small_data = [1, 2, 3]
    result = process_data(small_data)
    print(f"   处理 {small_data} 的结果项数: {len(result)}")
    print()
    
    # 测试问题 4
    print("4. 测试 process_user_data:")
    valid_user = {'name': 'Alice', 'age': 25, 'email': 'ALICE@EXAMPLE.COM'}
    print(f"   有效输入: {process_user_data(valid_user)}")
    # 以下情况会出错：
    # process_user_data("not a dict")  # 类型错误
    # process_user_data({'name': 'Bob'})  # 缺少键
    print()
    
    # 测试问题 5
    print("5. 测试 read_and_process_file:")
    print("   (需要创建测试文件来验证)")
    print()
    
    print("=== 练习结束：请找出并修复所有问题 ===")
