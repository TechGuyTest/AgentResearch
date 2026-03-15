"""
Unit Tests for Buggy Data Processor Module

These tests expose bugs in the buggy_data_processor.py module.
"""

import unittest
import sys
import os
import tempfile
import json

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice.buggy_data_processor import (
    add_user_to_list, calculate_average, find_duplicates,
    is_eligible_for_discount, load_config, build_message,
    save_data, get_timestamp, process_first_half, validate_input
)


class TestAddUserToList(unittest.TestCase):
    """Tests for add_user_to_list - BUG: Mutable default argument."""
    
    def test_add_user_to_list_independent_lists(self):
        """Test that each call creates an independent list."""
        # BUG: Current implementation shares the same default list
        users1 = add_user_to_list("Alice")
        users2 = add_user_to_list("Bob")
        
        # These should be independent lists
        self.assertEqual(users1, ["Alice"])
        self.assertEqual(users2, ["Bob"])
        self.assertIsNot(users1, users2)
    
    def test_add_user_to_list_multiple_calls(self):
        """Test multiple calls don't accumulate."""
        # BUG: Current implementation accumulates across calls
        users1 = add_user_to_list("Alice")
        users2 = add_user_to_list("Bob")
        users3 = add_user_to_list("Charlie")
        
        # Each should have exactly one user
        self.assertEqual(len(users1), 1)
        self.assertEqual(len(users2), 1)
        self.assertEqual(len(users3), 1)


class TestCalculateAverage(unittest.TestCase):
    """Tests for calculate_average - BUG: No handling for empty list."""
    
    def test_calculate_average_normal(self):
        """Test calculating average of normal list."""
        self.assertEqual(calculate_average([85, 90, 78, 92]), 86.25)
    
    def test_calculate_average_empty_list(self):
        """Test calculating average of empty list - should handle gracefully."""
        # BUG: Current implementation raises ZeroDivisionError
        # After fix, should raise ValueError with clear message
        with self.assertRaises(ValueError):
            calculate_average([])
    
    def test_calculate_average_single(self):
        """Test calculating average of single element."""
        self.assertEqual(calculate_average([42]), 42.0)


class TestFindDuplicates(unittest.TestCase):
    """Tests for find_duplicates - BUG: Inefficient O(n²) algorithm."""
    
    def test_find_duplicates_normal(self):
        """Test finding duplicates in normal list."""
        self.assertEqual(set(find_duplicates([1, 2, 3, 2, 4, 1, 5])), {1, 2})
    
    def test_find_duplicates_no_duplicates(self):
        """Test list with no duplicates."""
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])
    
    def test_find_duplicates_empty(self):
        """Test empty list."""
        self.assertEqual(find_duplicates([]), [])
    
    def test_find_duplicates_efficiency(self):
        """Test that function completes in reasonable time for large lists."""
        import time
        # BUG: Current O(n²) implementation will be very slow
        large_list = list(range(1000)) + list(range(500))
        start = time.time()
        result = find_duplicates(large_list)
        elapsed = time.time() - start
        
        # Should complete in under 0.1 seconds with efficient implementation
        self.assertLess(elapsed, 0.1, "find_duplicates should use efficient O(n) algorithm")
        self.assertEqual(len(result), 500)


class TestIsEligibleForDiscount(unittest.TestCase):
    """Tests for is_eligible_for_discount - BUG: Logic error in condition."""
    
    def test_member_always_eligible(self):
        """Test that members are always eligible."""
        self.assertTrue(is_eligible_for_discount(30, True))
        self.assertTrue(is_eligible_for_discount(25, True))
    
    def test_senior_eligible(self):
        """Test that seniors (>= 65) are eligible."""
        # BUG: Current implementation returns False for age 70
        self.assertTrue(is_eligible_for_discount(70, False))
        self.assertTrue(is_eligible_for_discount(65, False))
    
    def test_young_eligible(self):
        """Test that young people (<= 18) are eligible."""
        # BUG: Current implementation returns False for age 15
        self.assertTrue(is_eligible_for_discount(15, False))
        self.assertTrue(is_eligible_for_discount(18, False))
    
    def test_adult_non_member_not_eligible(self):
        """Test that adult non-members are not eligible."""
        self.assertFalse(is_eligible_for_discount(30, False))
        self.assertFalse(is_eligible_for_discount(40, False))


class TestLoadConfig(unittest.TestCase):
    """Tests for load_config - BUG: File not properly closed."""
    
    def test_load_config_valid_file(self):
        """Test loading valid config file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({"key": "value"}, f)
            temp_path = f.name
        
        try:
            config = load_config(temp_path)
            self.assertEqual(config["key"], "value")
        finally:
            os.unlink(temp_path)
    
    def test_load_config_file_not_found(self):
        """Test loading non-existent file - should handle gracefully."""
        # BUG: Current implementation raises FileNotFoundError without clear message
        with self.assertRaises(FileNotFoundError):
            load_config("/nonexistent/path/config.json")


class TestBuildMessage(unittest.TestCase):
    """Tests for build_message - BUG: Inefficient string concatenation."""
    
    def test_build_message_normal(self):
        """Test building normal message."""
        items = ["Apple", "Banana", "Cherry"]
        message = build_message(items)
        
        self.assertIn("Item 0: Apple", message)
        self.assertIn("Item 1: Banana", message)
        self.assertIn("Item 2: Cherry", message)
    
    def test_build_message_empty(self):
        """Test building message from empty list."""
        self.assertEqual(build_message([]), "")
    
    def test_build_message_efficiency(self):
        """Test that function is efficient for large lists."""
        import time
        # BUG: Current implementation using += is O(n²)
        large_list = ["item"] * 10000
        start = time.time()
        result = build_message(large_list)
        elapsed = time.time() - start
        
        # Should complete in under 0.1 seconds with efficient implementation
        self.assertLess(elapsed, 0.1, "build_message should use efficient string joining")


class TestSaveData(unittest.TestCase):
    """Tests for save_data - BUG: No exception handling."""
    
    def test_save_data_valid(self):
        """Test saving data to valid path."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            os.unlink(temp_path)  # Remove file so save_data can create it
            result = save_data({"key": "value"}, temp_path)
            self.assertTrue(result)
            
            # Verify file was created
            with open(temp_path, 'r') as f:
                content = json.load(f)
            self.assertEqual(content, {"key": "value"})
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_save_data_invalid_path(self):
        """Test saving to invalid path - should handle gracefully."""
        # BUG: Current implementation raises exception without handling
        with self.assertRaises((FileNotFoundError, PermissionError, OSError)):
            save_data({"key": "value"}, "/nonexistent/path/data.json")


class TestValidateInput(unittest.TestCase):
    """Tests for validate_input - BUG: Incorrect type comparison."""
    
    def test_validate_input_integer(self):
        """Test validating integer."""
        self.assertTrue(validate_input(42))
    
    def test_validate_input_float(self):
        """Test validating float."""
        self.assertTrue(validate_input(3.14))
    
    def test_validate_input_string(self):
        """Test validating string - should return False."""
        self.assertFalse(validate_input("42"))
    
    def test_validate_input_none(self):
        """Test validating None - should return False."""
        self.assertFalse(validate_input(None))
    
    def test_validate_input_boolean(self):
        """Test validating boolean - should return False."""
        self.assertFalse(validate_input(True))


class TestProcessFirstHalf(unittest.TestCase):
    """Tests for process_first_half - BUG: Unnecessary list copy."""
    
    def test_process_first_half_normal(self):
        """Test processing first half of list."""
        data = [1, 2, 3, 4, 5, 6]
        result = process_first_half(data)
        self.assertEqual(result, [2, 4, 6])
    
    def test_process_first_half_odd_length(self):
        """Test processing first half of odd-length list."""
        data = [1, 2, 3, 4, 5]
        result = process_first_half(data)
        self.assertEqual(result, [2, 4])


if __name__ == '__main__':
    unittest.main()
