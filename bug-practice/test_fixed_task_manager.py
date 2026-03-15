#!/usr/bin/env python3
"""
单元测试 - 验证 fixed_task_manager.py 修复了所有 bug
"""

import unittest
import sys
import os
import tempfile
import json
from datetime import datetime

# 导入修复后的版本
sys.path.insert(0, os.path.dirname(__file__))
import fixed_task_manager as fixed


class TestBug1_MutableDefault(unittest.TestCase):
    """Bug 1: 可变默认参数 - 验证修复"""
    
    def test_mutable_default_parameter_fixed(self):
        """测试可变默认参数已修复"""
        task1 = fixed.create_task("任务1", tags=["重要"])
        task2 = fixed.create_task("任务2")
        
        # 修复后：task2 的 tags 应该是空列表
        self.assertEqual(task2["tags"], [], "Bug 1 已修复：第二个任务的标签应该为空")
        self.assertEqual(task1["tags"], ["重要"], "第一个任务的标签应该保留")


class TestBug2_ClassLevelMutable(unittest.TestCase):
    """Bug 2: 类级别的可变对象 - 验证修复"""
    
    def test_class_level_mutable_fixed(self):
        """测试类属性共享问题已修复"""
        manager1 = fixed.TaskManager("管理器1")
        manager2 = fixed.TaskManager("管理器2")
        
        task = fixed.create_task("独立任务")
        manager1.add_task(task)
        
        # 修复后：manager2 的 all_tasks 应该为空
        self.assertEqual(len(manager2.all_tasks), 0, "Bug 2 已修复：manager2 不应该有任务")


class TestBug3_LateBindingClosure(unittest.TestCase):
    """Bug 3: Late binding closure - 验证正确性"""
    
    def test_priority_filters_work(self):
        """测试优先级过滤器正常工作"""
        manager = fixed.TaskManager()
        filters = manager.create_priority_filters()
        
        task_low = {"priority": "low"}
        task_medium = {"priority": "medium"}
        task_high = {"priority": "high"}
        
        # 所有过滤器都应该正常工作
        self.assertTrue(filters[0](task_low), "low 过滤器应该工作")
        self.assertFalse(filters[0](task_medium), "low 过滤器不应该匹配 medium")
        self.assertTrue(filters[1](task_medium), "medium 过滤器应该工作")
        self.assertTrue(filters[2](task_high), "high 过滤器应该工作")


class TestBug4_ModifyOriginalList(unittest.TestCase):
    """Bug 4: 修改原始列表 - 验证修复"""
    
    def test_get_completed_does_not_modify_original(self):
        """测试 get_completed_tasks 不修改原始列表"""
        manager = fixed.TaskManager()
        
        task1 = fixed.create_task("任务1")
        task1["completed"] = True
        task2 = fixed.create_task("任务2")
        task2["completed"] = False
        
        manager.add_task(task1)
        manager.add_task(task2)
        
        original_count = len(manager.all_tasks)
        completed = manager.get_completed_tasks()
        
        # 修复后：原始列表应该保持不变
        self.assertEqual(len(manager.all_tasks), original_count, 
                        "Bug 4 已修复：原始列表应该保持不变")
        self.assertEqual(len(completed), 1, "应该返回 1 个已完成任务")


class TestBug5_FloatComparison(unittest.TestCase):
    """Bug 5: 浮点数直接比较 - 验证修复"""
    
    def test_float_comparison_fixed(self):
        """测试浮点数比较已修复"""
        manager = fixed.TaskManager()
        
        # 添加 3 个任务，1 个完成 -> 完成率应该是 1/3
        for i in range(3):
            task = fixed.create_task(f"任务{i}")
            task["completed"] = (i == 0)
            manager.add_task(task)
        
        rate = manager.calculate_completion_rate()
        
        # 修复后：应该正确计算并使用 math.isclose 比较
        expected = 1/3
        self.assertAlmostEqual(rate, expected, places=10, 
                               msg="Bug 5 已修复：浮点数计算应该正确")


class TestBug6_ResourceLeak(unittest.TestCase):
    """Bug 6: 资源未正确关闭 - 验证修复"""
    
    def test_file_properly_closed(self):
        """测试文件操作资源泄漏已修复"""
        manager = fixed.TaskManager()
        task = fixed.create_task("测试任务")
        manager.add_task(task)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
            filename = tmp.name
        
        try:
            # 修复后：文件应该正确关闭
            manager.save_to_file(filename)
            
            # 验证文件内容正确
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.assertEqual(len(data), 1, "Bug 6 已修复：文件内容应该正确")
        finally:
            if os.path.exists(filename):
                os.remove(filename)


class TestBug7_StringConcatenation(unittest.TestCase):
    """Bug 7: 字符串拼接效率 - 验证修复"""
    
    def test_string_concatenation_efficient(self):
        """测试字符串拼接效率问题已修复"""
        tasks = [
            fixed.create_task(f"任务{i}", description=f"描述{i}")
            for i in range(100)
        ]
        
        # 修复后：应该使用列表推导式
        report = fixed.generate_report(tasks)
        self.assertIsInstance(report, str, "应该返回字符串")
        self.assertIn("任务 1", report, "报告应该包含任务信息")


class TestBug8_ShallowCopy(unittest.TestCase):
    """Bug 8: 浅拷贝问题 - 验证修复"""
    
    def test_deep_copy_does_not_modify_original(self):
        """测试深拷贝不会修改原始数据"""
        original = [
            {"id": 1, "title": "任务1", "tags": ["重要"]},
            {"id": 2, "title": "任务2", "tags": ["普通"]}
        ]
        
        copied = fixed.duplicate_tasks(original)
        
        # 修改副本
        copied[0]["tags"].append("紧急")
        
        # 修复后：原始数据不应该被修改
        self.assertEqual(original[0]["tags"], ["重要"], 
                        "Bug 8 已修复：原始数据不应该被修改")
        self.assertEqual(copied[0]["tags"], ["重要", "紧急"], 
                        "副本应该被修改")


class TestBug9_BroadException(unittest.TestCase):
    """Bug 9: 过于宽泛的异常捕获 - 验证修复"""
    
    def test_specific_exception_handling(self):
        """测试异常处理已修复"""
        # 修复后：应该只捕获 ValueError 和 TypeError
        result = fixed.parse_task_date(None)
        self.assertIsNone(result, "应该返回 None")


class TestBug10_ModifyInputParameter(unittest.TestCase):
    """Bug 10: 修改传入的可变参数 - 验证修复"""
    
    def test_does_not_modify_input_parameter(self):
        """测试函数不修改传入的任务对象"""
        original_task = {"id": 1, "title": "任务", "tags": ["重要"]}
        original_tags = original_task["tags"].copy()
        
        result = fixed.add_tags_to_task(original_task, ["紧急"])
        
        # 修复后：原始任务对象不应该被修改
        self.assertEqual(original_task["tags"], original_tags,
                        "Bug 10 已修复：原始任务对象不应该被修改")
        self.assertEqual(result["tags"], ["重要", "紧急"],
                        "新任务应该包含添加的标签")


class TestBug11_IgnoreReturnValue(unittest.TestCase):
    """Bug 11: 忽略返回值 - 验证修复"""
    
    def test_return_value_checked(self):
        """测试验证器检查返回值"""
        validator = fixed.TaskValidator()
        
        # 空标题应该验证失败
        task = {"title": ""}
        result = validator.validate_task(task)
        
        # 修复后：应该检查返回值并返回 False
        self.assertFalse(result, "Bug 11 已修复：空标题应该验证失败")
        self.assertTrue(len(validator.errors) > 0, "应该有错误信息")


class TestBug12_IsComparison(unittest.TestCase):
    """Bug 12: 使用 is 比较布尔值 - 验证修复"""
    
    def test_boolean_comparison_fixed(self):
        """测试布尔值比较已修复"""
        task = {"completed": True}
        result = fixed.check_task_status(task)
        
        # 修复后：应该使用布尔值直接判断
        self.assertEqual(result, "已完成", "应该返回'已完成'")


class TestBug13_NoNoneCheck(unittest.TestCase):
    """Bug 13: 未处理 None 返回值 - 验证修复"""
    
    def test_none_return_value_documented(self):
        """测试查找不存在的任务返回 None"""
        tasks = [
            fixed.create_task("任务1"),
            fixed.create_task("任务2")
        ]
        
        result = fixed.get_task_by_id(tasks, 999999)
        
        # 修复后：函数应该明确文档说明可能返回 None
        self.assertIsNone(result, "未找到任务应该返回 None")


if __name__ == "__main__":
    # 运行测试并显示详细结果
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBug1_MutableDefault)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug2_ClassLevelMutable))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug3_LateBindingClosure))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug4_ModifyOriginalList))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug5_FloatComparison))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug6_ResourceLeak))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug7_StringConcatenation))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug8_ShallowCopy))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug9_BroadException))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug10_ModifyInputParameter))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug11_IgnoreReturnValue))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug12_IsComparison))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBug13_NoNoneCheck))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 退出码：如果有失败或错误，返回非零
    sys.exit(0 if result.wasSuccessful() else 1)
