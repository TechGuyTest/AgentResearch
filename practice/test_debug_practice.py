"""
单元测试文件 - 测试 debug_practice_exercise.py 中的所有问题
"""
import unittest
import tempfile
import os
from debug_practice_exercise import (
    add_item_to_list,
    calculate_average,
    find_duplicates,
    is_valid_age,
    read_file_content,
    find_user_by_name,
    is_close_to_zero
)


class TestDebugPractice(unittest.TestCase):
    
    # ============================================================
    # 测试问题 1: 可变默认参数陷阱
    # ============================================================
    def test_add_item_to_list_mutable_default(self):
        """测试可变默认参数问题 - 每次调用应该得到独立的列表"""
        result1 = add_item_to_list(1)
        result2 = add_item_to_list(2)
        
        # 预期：两个调用应该返回不同的列表
        self.assertIsNot(result1, result2, "每次调用应该返回不同的列表对象")
        
        # 预期：第一次调用应该只包含 [1]
        self.assertEqual(result1, [1], f"第一次调用应该返回 [1]，实际: {result1}")
        
        # 预期：第二次调用应该只包含 [2]
        self.assertEqual(result2, [2], f"第二次调用应该返回 [2]，实际: {result2}")
    
    def test_add_item_to_list_with_custom_list(self):
        """测试传入自定义列表时的行为"""
        custom_list = [10, 20]
        result = add_item_to_list(30, custom_list)
        self.assertEqual(result, [10, 20, 30])
        self.assertIs(result, custom_list)
    
    # ============================================================
    # 测试问题 2: 边界情况未处理 - 除零错误
    # ============================================================
    def test_calculate_average_empty_list(self):
        """测试空列表应该抛出异常或返回 None"""
        with self.assertRaises((ZeroDivisionError, ValueError, TypeError)):
            calculate_average([])
    
    def test_calculate_average_single_element(self):
        """测试单个元素的列表"""
        self.assertEqual(calculate_average([5]), 5.0)
    
    def test_calculate_average_multiple_elements(self):
        """测试多个元素的列表"""
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    
    def test_calculate_average_negative_numbers(self):
        """测试包含负数的列表"""
        self.assertAlmostEqual(calculate_average([-1, 0, 1]), 0.0)
    
    # ============================================================
    # 测试问题 3: 低效的列表查找模式
    # ============================================================
    def test_find_duplicates_no_duplicates(self):
        """测试没有重复项的情况"""
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])
    
    def test_find_duplicates_with_duplicates(self):
        """测试有重复项的情况"""
        self.assertEqual(find_duplicates([1, 2, 3, 2, 4, 3, 5]), [2, 3])
    
    def test_find_duplicates_all_same(self):
        """测试所有元素都相同的情况"""
        self.assertEqual(find_duplicates([1, 1, 1, 1]), [1])
    
    def test_find_duplicates_performance(self):
        """测试性能 - 应该能处理较大列表"""
        large_list = list(range(100)) + list(range(50))
        result = find_duplicates(large_list)
        self.assertEqual(len(result), 50)
        self.assertTrue(all(x in result for x in range(50)))
    
    # ============================================================
    # 测试问题 4: 逻辑错误 - 条件判断错误
    # ============================================================
    def test_is_valid_age_valid(self):
        """测试有效的年龄"""
        self.assertTrue(is_valid_age(25), "25 应该是有效的年龄")
        self.assertTrue(is_valid_age(0), "0 应该是有效的年龄（边界）")
        self.assertTrue(is_valid_age(150), "150 应该是有效的年龄（边界）")
    
    def test_is_valid_age_invalid(self):
        """测试无效的年龄"""
        self.assertFalse(is_valid_age(-1), "-1 应该是无效的年龄")
        self.assertFalse(is_valid_age(151), "151 应该是无效的年龄")
        self.assertFalse(is_valid_age(200), "200 应该是无效的年龄")
    
    def test_is_valid_age_edge_cases(self):
        """测试边界情况"""
        self.assertTrue(is_valid_age(1), "1 应该是有效的年龄")
        self.assertTrue(is_valid_age(149), "149 应该是有效的年龄")
    
    # ============================================================
    # 测试问题 5: 文件资源未正确关闭
    # ============================================================
    def test_read_file_content_normal(self):
        """测试正常读取文件"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("line 1\nline 2\nline 3\n")
            temp_path = f.name
        
        try:
            lines = read_file_content(temp_path)
            self.assertEqual(len(lines), 3)
            self.assertEqual(lines[0], "line 1\n")
        finally:
            os.unlink(temp_path)
    
    def test_read_file_content_empty_file(self):
        """测试读取空文件"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            temp_path = f.name
        
        try:
            lines = read_file_content(temp_path)
            self.assertEqual(lines, [])
        finally:
            os.unlink(temp_path)
    
    def test_read_file_content_with_exception(self):
        """测试文件不存在时的异常处理"""
        with self.assertRaises(FileNotFoundError):
            read_file_content("/nonexistent/file.txt")
    
    # ============================================================
    # 测试问题 6: 字符串比较错误
    # ============================================================
    def test_find_user_by_name_found(self):
        """测试找到用户的情况"""
        users = [{'name': 'Alice', 'id': 1}, {'name': 'Bob', 'id': 2}]
        result = find_user_by_name(users, 'Alice')
        self.assertIsNotNone(result, "应该找到用户 Alice")
        self.assertEqual(result['id'], 1)
    
    def test_find_user_by_name_not_found(self):
        """测试未找到用户的情况"""
        users = [{'name': 'Alice', 'id': 1}]
        result = find_user_by_name(users, 'Charlie')
        self.assertIsNone(result, "应该返回 None")
    
    def test_find_user_by_name_same_value_different_object(self):
        """测试相同值但不同对象的字符串"""
        users = [{'name': 'Alice', 'id': 1}]
        # 创建一个新的字符串对象，内容相同
        target_name = ''.join(['A', 'l', 'i', 'c', 'e'])
        result = find_user_by_name(users, target_name)
        self.assertIsNotNone(result, "应该找到用户，即使字符串是不同对象")
        self.assertEqual(result['name'], 'Alice')
    
    # ============================================================
    # 测试问题 7: 浮点数比较问题
    # ============================================================
    def test_is_close_to_zero_exact_zero(self):
        """测试精确的零"""
        self.assertTrue(is_close_to_zero(0.0), "0.0 应该被认为是接近零")
    
    def test_is_close_to_zero_small_values(self):
        """测试很小的值应该被认为是接近零"""
        self.assertTrue(is_close_to_zero(0.00001), "0.00001 应该被认为是接近零")
        self.assertTrue(is_close_to_zero(1e-10), "1e-10 应该被认为是接近零")
        self.assertTrue(is_close_to_zero(-0.00001), "-0.00001 应该被认为是接近零")
    
    def test_is_close_to_zero_large_values(self):
        """测试较大的值不应该被认为是接近零"""
        self.assertFalse(is_close_to_zero(0.1), "0.1 不应该被认为是接近零")
        self.assertFalse(is_close_to_zero(1.0), "1.0 不应该被认为是接近零")
        self.assertFalse(is_close_to_zero(-0.1), "-0.1 不应该被认为是接近零")


if __name__ == '__main__':
    unittest.main(verbosity=2)
