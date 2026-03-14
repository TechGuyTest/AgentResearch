"""
Unit Tests for Data Processor Module

These tests expose bugs in the data_processor.py module.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice.data_processor import (
    calculate_average, find_max_value, process_user_scores,
    filter_valid_emails, merge_and_sort_lists, count_word_occurrences
)


class TestCalculateAverage(unittest.TestCase):
    """Tests for the calculate_average function."""
    
    def test_calculate_average_normal(self):
        """Test calculating average of normal list."""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    
    def test_calculate_average_single(self):
        """Test calculating average of single element."""
        self.assertEqual(calculate_average([5]), 5.0)
    
    def test_calculate_average_empty(self):
        """Test calculating average of empty list - should handle gracefully."""
        with self.assertRaises(ValueError):
            calculate_average([])


class TestFindMaxValue(unittest.TestCase):
    """Tests for the find_max_value function."""
    
    def test_find_max_value_normal(self):
        """Test finding max in normal list."""
        self.assertEqual(find_max_value([1, 5, 3, 9, 2]), 9)
    
    def test_find_max_value_negative(self):
        """Test finding max in negative numbers."""
        self.assertEqual(find_max_value([-5, -2, -10, -1]), -1)
    
    def test_find_max_value_empty(self):
        """Test finding max in empty list."""
        self.assertIsNone(find_max_value([]))
    
    def test_find_max_value_single(self):
        """Test finding max in single element list."""
        self.assertEqual(find_max_value([42]), 42)


class TestProcessUserScores(unittest.TestCase):
    """Tests for the process_user_scores function."""
    
    def test_process_user_scores_normal(self):
        """Test processing normal scores."""
        scores = [85, 72, 59, 90, 60, 45, 78]
        result = process_user_scores(scores)
        
        # 60 should be passing (>= 60)
        self.assertIn(60, result['passed'])
        self.assertNotIn(60, result['failed'])
        
        # 59 should be failing (< 60)
        self.assertIn(59, result['failed'])
        self.assertNotIn(59, result['passed'])
    
    def test_process_user_scores_boundary(self):
        """Test boundary condition at exactly 60."""
        scores = [60]
        result = process_user_scores(scores)
        self.assertEqual(result['passed'], [60])
        self.assertEqual(result['failed'], [])
    
    def test_process_user_scores_empty(self):
        """Test processing empty scores list - should handle gracefully."""
        with self.assertRaises(ValueError):
            process_user_scores([])


class TestFilterValidEmails(unittest.TestCase):
    """Tests for the filter_valid_emails function."""
    
    def test_filter_valid_emails_normal(self):
        """Test filtering normal emails."""
        emails = ["user@example.com", "test@domain.org"]
        valid = filter_valid_emails(emails)
        self.assertEqual(len(valid), 2)
    
    def test_filter_valid_emails_invalid(self):
        """Test filtering invalid emails."""
        emails = ["invalid", "noat.com"]
        valid = filter_valid_emails(emails)
        self.assertEqual(len(valid), 0)
    
    def test_filter_valid_emails_empty_string(self):
        """Test filtering empty string - should be rejected."""
        emails = ["", "valid@test.com"]
        valid = filter_valid_emails(emails)
        self.assertNotIn("", valid)
        self.assertEqual(len(valid), 1)
    
    def test_filter_valid_emails_whitespace(self):
        """Test filtering whitespace-only strings - should be rejected."""
        emails = ["   ", "valid@test.com"]
        valid = filter_valid_emails(emails)
        self.assertNotIn("   ", valid)
        self.assertEqual(len(valid), 1)
    
    def test_filter_valid_emails_missing_at(self):
        """Test filtering emails without @ - should be rejected."""
        emails = ["nodomain.com", "valid@test.com"]
        valid = filter_valid_emails(emails)
        self.assertNotIn("nodomain.com", valid)


class TestMergeAndSortLists(unittest.TestCase):
    """Tests for the merge_and_sort_lists function."""
    
    def test_merge_and_sort_lists_normal(self):
        """Test merging and sorting normal lists."""
        list1 = [3, 1, 4]
        list2 = [2, 5, 6]
        result = merge_and_sort_lists(list1, list2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_merge_and_sort_lists_empty(self):
        """Test merging with empty lists."""
        self.assertEqual(merge_and_sort_lists([], []), [])
        self.assertEqual(merge_and_sort_lists([1, 2], []), [1, 2])
        self.assertEqual(merge_and_sort_lists([], [3, 4]), [3, 4])
    
    def test_merge_and_sort_lists_does_not_modify_original(self):
        """Test that original lists are not modified."""
        list1 = [3, 1, 4]
        list2 = [2, 5, 6]
        original1 = list1.copy()
        original2 = list2.copy()
        merge_and_sort_lists(list1, list2)
        self.assertEqual(list1, original1)
        self.assertEqual(list2, original2)


class TestCountWordOccurrences(unittest.TestCase):
    """Tests for the count_word_occurrences function."""
    
    def test_count_word_occurrences_normal(self):
        """Test counting word occurrences normally."""
        text = "The cat sat on the cat mat"
        self.assertEqual(count_word_occurrences(text, "cat"), 2)
    
    def test_count_word_occurrences_case_insensitive(self):
        """Test counting should be case insensitive."""
        text = "The Cat sat on the CAT mat"
        self.assertEqual(count_word_occurrences(text, "cat"), 2)
    
    def test_count_word_occurrences_no_partial_matches(self):
        """Test that partial matches are not counted."""
        text = "The cat sat on the cathedral"
        # "cat" should not match "cathedral"
        self.assertEqual(count_word_occurrences(text, "cat"), 1)
    
    def test_count_word_occurrences_not_found(self):
        """Test counting word not in text."""
        text = "The dog ran in the park"
        self.assertEqual(count_word_occurrences(text, "cat"), 0)


if __name__ == '__main__':
    unittest.main()
