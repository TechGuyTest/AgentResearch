"""
Unit Tests for Data Structures Module

These tests expose bugs in the data_structures.py module.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice.data_structures import (
    find_max, find_min, binary_search, merge_dicts,
    flatten_list, remove_element, count_occurrences
)


class TestFindMax(unittest.TestCase):
    """Tests for the find_max function."""
    
    def test_find_max_positive_numbers(self):
        """Test finding max in positive numbers."""
        self.assertEqual(find_max([1, 5, 3, 9, 2]), 9)
    
    def test_find_max_negative_numbers(self):
        """Test finding max in negative numbers - BUG: Current implementation fails."""
        self.assertEqual(find_max([-5, -2, -10, -1]), -1)  # BUG: Returns 0 instead
    
    def test_find_max_mixed_numbers(self):
        """Test finding max in mixed numbers."""
        self.assertEqual(find_max([-5, 0, 5, -10]), 5)
    
    def test_find_max_empty_list(self):
        """Test finding max in empty list."""
        self.assertIsNone(find_max([]))
    
    def test_find_max_single_element(self):
        """Test finding max in single element list."""
        self.assertEqual(find_max([42]), 42)


class TestFindMin(unittest.TestCase):
    """Tests for the find_min function."""
    
    def test_find_min_positive_numbers(self):
        """Test finding min in positive numbers."""
        self.assertEqual(find_min([5, 2, 8, 1, 9]), 1)
    
    def test_find_min_negative_numbers(self):
        """Test finding min in negative numbers - BUG: Current implementation fails."""
        self.assertEqual(find_min([-5, -2, -10, -1]), -10)  # BUG: Returns 0 instead
    
    def test_find_min_mixed_numbers(self):
        """Test finding min in mixed numbers."""
        self.assertEqual(find_min([-5, 0, 5, -10]), -10)
    
    def test_find_min_empty_list(self):
        """Test finding min in empty list."""
        self.assertIsNone(find_min([]))
    
    def test_find_min_single_element(self):
        """Test finding min in single element list."""
        self.assertEqual(find_min([42]), 42)


class TestBinarySearch(unittest.TestCase):
    """Tests for the binary_search function."""
    
    def test_binary_search_found(self):
        """Test binary search when element is found."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
    
    def test_binary_search_not_found(self):
        """Test binary search when element is not found."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
    
    def test_binary_search_first_element(self):
        """Test binary search for first element."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
    
    def test_binary_search_last_element(self):
        """Test binary search for last element."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)
    
    def test_binary_search_empty_list(self):
        """Test binary search on empty list."""
        self.assertEqual(binary_search([], 1), -1)
    
    def test_binary_search_infinite_loop(self):
        """Test that binary search doesn't cause infinite loop - BUG: Current implementation does."""
        # This should complete quickly, not hang
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
        self.assertEqual(result, 6)


class TestMergeDicts(unittest.TestCase):
    """Tests for the merge_dicts function."""
    
    def test_merge_dicts_normal(self):
        """Test merging two dictionaries."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(result, {"a": 1, "b": 2, "c": 3, "d": 4})
    
    def test_merge_dicts_no_side_effects(self):
        """Test that merge_dicts doesn't modify original dict1 - BUG: Current implementation does."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}
        original_dict1 = dict1.copy()
        merge_dicts(dict1, dict2)
        self.assertEqual(dict1, original_dict1)  # BUG: dict1 is modified
    
    def test_merge_dicts_overlapping_keys(self):
        """Test merging dictionaries with overlapping keys."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(result, {"a": 1, "b": 3, "c": 4})
    
    def test_merge_dicts_empty(self):
        """Test merging empty dictionaries."""
        self.assertEqual(merge_dicts({}, {}), {})


class TestFlattenList(unittest.TestCase):
    """Tests for the flatten_list function."""
    
    def test_flatten_list_simple(self):
        """Test flattening a simple nested list."""
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])
    
    def test_flatten_list_deeply_nested(self):
        """Test flattening a deeply nested list - BUG: Current implementation fails."""
        # BUG: Current implementation only handles one level of nesting
        self.assertEqual(flatten_list([1, [2, [3, [4]]]]), [1, 2, 3, 4])
    
    def test_flatten_list_empty(self):
        """Test flattening an empty list."""
        self.assertEqual(flatten_list([]), [])
    
    def test_flatten_list_no_nesting(self):
        """Test flattening a list with no nesting."""
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])


class TestRemoveElement(unittest.TestCase):
    """Tests for the remove_element function."""
    
    def test_remove_element_single(self):
        """Test removing a single occurrence."""
        lst = [1, 2, 3, 2, 4]
        result = remove_element(lst.copy(), 3)
        self.assertEqual(result, [1, 2, 2, 4])
    
    def test_remove_element_multiple(self):
        """Test removing multiple occurrences - BUG: Current implementation fails."""
        lst = [1, 2, 2, 2, 3]
        result = remove_element(lst.copy(), 2)
        self.assertEqual(result, [1, 3])  # BUG: May skip elements due to modifying during iteration
    
    def test_remove_element_not_present(self):
        """Test removing element not in list."""
        lst = [1, 2, 3]
        result = remove_element(lst.copy(), 5)
        self.assertEqual(result, [1, 2, 3])
    
    def test_remove_element_does_not_modify_original(self):
        """Test that remove_element doesn't modify original list - BUG: Current implementation does."""
        lst = [1, 2, 3, 2, 4]
        original = lst.copy()
        remove_element(lst, 2)
        self.assertEqual(lst, original)  # BUG: Original list is modified


class TestCountOccurrences(unittest.TestCase):
    """Tests for the count_occurrences function."""
    
    def test_count_occurrences_normal(self):
        """Test counting occurrences normally."""
        self.assertEqual(count_occurrences([1, 2, 2, 3, 2], 2), 3)
    
    def test_count_occurrences_not_present(self):
        """Test counting element not in list."""
        self.assertEqual(count_occurrences([1, 2, 3], 5), 0)
    
    def test_count_occurrences_empty_list(self):
        """Test counting in empty list."""
        self.assertEqual(count_occurrences([], 1), 0)
    
    def test_count_occurrences_all_same(self):
        """Test counting when all elements are the same."""
        self.assertEqual(count_occurrences([5, 5, 5, 5], 5), 4)


if __name__ == '__main__':
    unittest.main()
