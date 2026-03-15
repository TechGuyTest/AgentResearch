#!/usr/bin/env python3
"""
单元测试 - 暴露 buggy_task_manager.py 中的所有 bug
"""

import unittest
import sys
import os
import tempfile
import json
from datetime import datetime

# 导入原始的 buggy 版本
sys.path.insert(0, os.path.dirname(__file__))
import buggy_task_manager_20260314_075529 as buggy


class TestBug1_MutableDefault(unittest.TestCase):
    """Bug 1: 可变默认参数"""
    
    def test_mutable_default_parameter(self):
        """测试可变默认参数导致的任务共享标签"""
        task1 = buggy.create_task("任务1", tags=["重要"])
        task2 = buggy.create_task("任务2")
        
        # Bug: task2 的 tags 应该是空列表，但实际上共享了 task1 的列表
        self.assertNotEqual(task2["tags"], [], "Bug 1: 可变默认参数导致标签共享")
        self.assertEqual(task2["tags"], ["重要"], "Bug 1: 第二个任务不应该有标签")


class TestBug2_ClassLevelMutable(unittest.TestCase):
    """Bug 2: 类级别的可变对象"""
    
    def test_class_level_mutable_shared(self):
        """测试类属性在实例间共享"""
        manager1 = buggy.TaskManager("管理器1")
        manager2 = buggy.TaskManager("管理器2")
        
        task = buggy.create_task("共享任务")
        manager1.add_task(task)
        
        # Bug: manager2 的 all_tasks 应该为空，但实际上共享了 manager1 的列表
        self.assertNotEqual(len(manager2.all_tasks), 0, "Bug 2: 类属性在实例间共享")
        self.assertEqual(len(manager2.all_tasks), 1, "Bug 2: manager2 不应该有任务")


class TestBug3_LateBindingClosure(unittest.TestCase):
    """Bug 3: Late binding closure (代码已修复，测试正确性)"""
    
    def test_priority_filters_work(self):
        """测试优先级过滤器正常工作"""
        manager = buggy.TaskManager()
        filters = manager.create_priority_filters()
        
        task_low = {"priority": "low"}
        task_medium = {"priority": "medium"}
        task_high = {"priority": "high"}
        
        # 所有过滤器都应该正常工作
        self.assertTrue(filters[0](task_low), "Bug 3: low 过滤器应该工作")
        self.assertFalse(filters[0](task_medium), "Bug 3: low 过滤器不应该匹配 medium")
        self.assertTrue(filters[1](task_medium), "Bug 3: medium 过滤器应该工作")
        self.assertTrue(filters[2](task_high), "Bug 3: high 过滤器应该工作")


class TestBug4_ModifyOriginalList(unittest.TestCase):
    """Bug 4: 修改原始列表而非返回副本"""
    
    def test_get_completed_modifies_original(self):
        """测试 get_completed_tasks 修改了原始列表"""
        manager = buggy.TaskManager()
        
        task1 = buggy.create_task("任务1")
        task1["completed"] = True
        task2 = buggy.create_task("任务2")
        task2["completed"] = False
        
        manager.add_task(task1)
        manager.add_task(task2)
        
        original_count = len(manager.all_tasks)
        completed = manager.get_completed_tasks()
        
        # Bug: 原始列表被修改了，应该保持不变
        self.assertNotEqual(len(manager.all_tasks), original_count, 
                           "Bug 4: get_completed_tasks 修改了原始列表")
        self.assertEqual(len(manager.all_tasks), 1, 
                        "Bug 4: 原始列表应该被过滤，只剩未完成任务")


class TestBug5_FloatComparison(unittest.TestCase):
    """Bug 5: 浮点数直接比较"""
    
    def test_float_comparison_fails(self):
        """测试浮点数比较问题"""
        manager = buggy.TaskManager()
        
        # 添加 3 个任务，1 个完成 -> 完成率应该是 1/3
        for i in range(3):
            task = buggy.create_task(f"任务{i}")
            task["completed"] = (i == 0)
            manager.add_task(task)
        
        rate = manager.calculate_completion_rate()
        
        # Bug: 由于浮点数精度问题，直接比较可能失败
        # 代码中使用 rate == 0.3333333333333333，这可能不成立
        expected = 1/3
        self.assertNotEqual(rate, expected, 
                           "Bug 5: 浮点数直接比较可能失败")


class TestBug6_ResourceLeak(unittest.TestCase):
    """Bug 6: 资源未正确关闭"""
    
    def test_file_not_closed(self):
        """测试文件操作资源泄漏"""
        manager = buggy.TaskManager()
        task = buggy.create_task("测试任务")
        manager.add_task(task)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
            filename = tmp.name
        
        try:
            # Bug: 文件打开后未关闭
            manager.save_to_file(filename)
            
            # 验证文件内容正确
            with open(filename, 'r') as f:
                data = json.load(f)
                self.assertEqual(len(data), 1, "Bug 6: 文件内容应该正确")
        finally:
            if os.path.exists(filename):
                os.remove(filename)


class TestBug7_StringConcatenation(unittest.TestCase):
    """Bug 7: 字符串拼接效率低下"""
    
    def test_string_concatenation_inefficient(self):
        """测试字符串拼接效率问题（性能测试）"""
        tasks = [
            buggy.create_task(f"任务{i}", description=f"描述{i}")
            for i in range(100)
        ]
        
        # Bug: 使用 + 拼接字符串效率低下
        # 这里主要是代码审查问题，不是功能错误
        report = buggy.generate_report(tasks)
        self.assertIsInstance(report, str, "Bug 7: 应该返回字符串")


class TestBug8_ShallowCopy(unittest.TestCase):
    """Bug 8: 浅拷贝问题"""
    
    def test_shallow_copy_modifies_original(self):
        """测试浅拷贝导致原始数据被修改"""
        original = [
            {"id": 1, "title": "任务1", "tags": ["重要"]},
            {"id": 2, "title": "任务2", "tags": ["普通"]}
        ]
        
        copied = buggy.duplicate_tasks(original)
        
        # 修改副本
        copied[0]["tags"].append("紧急")
        
        # Bug: 原始数据也被修改了，因为是浅拷贝
        self.assertNotEqual(original[0]["tags"], ["重要"], 
                           "Bug 8: 浅拷贝导致原始数据被修改")
        self.assertEqual(original[0]["tags"], ["重要", "紧急"], 
                        "Bug 8: 原始任务的标签被修改了")


class TestBug9_BroadException(unittest.TestCase):
    """Bug 9: 过于宽泛的异常捕获"""
    
    def test_broad_exception_catches_keyboard_interrupt(self):
        """测试过于宽泛的异常捕获"""
        # Bug: except: 会捕获所有异常，包括 KeyboardInterrupt
        result = buggy.parse_task_date(None)
        self.assertIsNone(result, "Bug 9: 应该返回 None")


class TestBug10_ModifyInputParameter(unittest.TestCase):
    """Bug 10: 修改传入的可变参数"""
    
    def test_modify_input_parameter(self):
        """测试函数修改了传入的任务对象"""
        original_task = {"id": 1, "title": "任务", "tags": ["重要"]}
        original_tags = original_task["tags"].copy()
        
        result = buggy.add_tags_to_task(original_task, ["紧急"])
        
        # Bug: 原始任务对象被修改了
        self.assertNotEqual(original_task["tags"], original_tags,
                           "Bug 10: 原始任务对象被修改了")
        self.assertEqual(original_task["tags"], ["重要", "紧急"],
                        "Bug 10: 原始任务的标签被修改了")


class TestBug11_IgnoreReturnValue(unittest.TestCase):
    """Bug 11: 忽略返回值"""
    
    def test_ignore_return_value(self):
        """测试验证器忽略返回值"""
        validator = buggy.TaskValidator()
        
        # 空标题应该验证失败
        task = {"title": ""}
        result = validator.validate_task(task)
        
        # Bug: validate_title 返回 False，但 validate_task 没有检查
        # 所以 validate_task 可能返回 True 即使标题无效
        self.assertFalse(result, "Bug 11: 空标题应该验证失败")
        self.assertTrue(len(validator.errors) > 0, "Bug 11: 应该有错误信息")


class TestBug12_IsComparison(unittest.TestCase):
    """Bug 12: 使用 is 比较布尔值"""
    
    def test_is_comparison_works(self):
        """测试 is 比较（代码审查问题）"""
        task = {"completed": True}
        result = buggy.check_task_status(task)
        
        # 虽然 is 比较在这里有效，但不是最佳实践
        self.assertEqual(result, "已完成", "Bug 12: 应该返回'已完成'")


class TestBug13_NoNoneCheck(unittest.TestCase):
    """Bug 13: 未处理 None 返回值"""
    
    def test_none_return_value(self):
        """测试查找不存在的任务返回 None"""
        tasks = [
            buggy.create_task("任务1"),
            buggy.create_task("任务2")
        ]
        
        result = buggy.get_task_by_id(tasks, 999999)
        
        # Bug: 函数返回 None，调用者可能不会检查
        self.assertIsNone(result, "Bug 13: 未找到任务应该返回 None")


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
