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
        self.assertEqual(calculate_average([10]), 10.0)
    
    def test_calculate_average_empty_list(self):
        """Test calculating average of empty list - should handle gracefully."""
        # BUG: Current implementation raises ZeroDivisionError
        with self.assertRaises(ValueError):
            calculate_average([])


class TestFindMaxValue(unittest.TestCase):
    """Tests for the find_max_value function."""
    
    def test_find_max_value_normal(self):
        """Test finding max value in normal list."""
        self.assertEqual(find_max_value([1, 5, 3, 9, 2]), 9)
    
    def test_find_max_value_negative(self):
        """Test finding max value in negative numbers."""
        self.assertEqual(find_max_value([-5, -2, -10, -1]), -1)
    
    def test_find_max_value_empty(self):
        """Test finding max value in empty list."""
        self.assertIsNone(find_max_value([]))
    
    def test_find_max_value_single(self):
        """Test finding max value in single element list."""
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
    
    def test_process_user_scores_boundary(self):
        """Test boundary condition at 60."""
        scores = [59, 60, 61]
        result = process_user_scores(scores)
        # 59 should fail, 60 and 61 should pass
        self.assertIn(59, result['failed'])
        self.assertIn(60, result['passed'])
        self.assertIn(61, result['passed'])
    
    def test_process_user_scores_empty(self):
        """Test processing empty scores list - should handle gracefully."""
        # BUG: Current implementation raises ZeroDivisionError
        with self.assertRaises(ValueError):
            process_user_scores([])


class TestFilterValidEmails(unittest.TestCase):
    """Tests for the filter_valid_emails function."""
    
    def test_filter_valid_emails_normal(self):
        """Test filtering normal email list."""
        emails = ["user@example.com", "test@domain.org"]
        result = filter_valid_emails(emails)
        self.assertEqual(len(result), 2)
    
    def test_filter_valid_emails_invalid(self):
        """Test filtering out invalid emails."""
        emails = ["invalid", "no-at-sign.com"]
        result = filter_valid_emails(emails)
        self.assertEqual(len(result), 0)
    
    def test_filter_valid_emails_empty_string(self):
        """Test filtering out empty strings - should not be considered valid."""
        emails = ["", "user@example.com"]
        result = filter_valid_emails(emails)
        # BUG: Current implementation may include empty string
        self.assertNotIn("", result)
        self.assertEqual(len(result), 1)
    
    def test_filter_valid_emails_whitespace(self):
        """Test filtering out whitespace-only strings."""
        emails = ["   ", "user@example.com"]
        result = filter_valid_emails(emails)
        # BUG: Current implementation may include whitespace
        self.assertNotIn("   ", result)
        self.assertEqual(len(result), 1)
    
    def test_filter_valid_emails_malformed(self):
        """Test filtering malformed emails like ' @bad.com'."""
        emails = [" @bad.com", "user@example.com"]
        result = filter_valid_emails(emails)
        # BUG: Current implementation may include malformed emails
        self.assertNotIn(" @bad.com", result)
        self.assertEqual(len(result), 1)


class TestMergeAndSortLists(unittest.TestCase):
    """Tests for the merge_and_sort_lists function."""
    
    def test_merge_and_sort_lists_normal(self):
        """Test merging and sorting normal lists."""
        list1 = [3, 1, 2]
        list2 = [6, 4, 5]
        result = merge_and_sort_lists(list1, list2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_merge_and_sort_lists_empty(self):
        """Test merging with empty lists."""
        self.assertEqual(merge_and_sort_lists([], []), [])
        self.assertEqual(merge_and_sort_lists([1, 2], []), [1, 2])
        self.assertEqual(merge_and_sort_lists([], [3, 4]), [3, 4])
    
    def test_merge_and_sort_lists_duplicates(self):
        """Test merging lists with duplicates."""
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        result = merge_and_sort_lists(list1, list2)
        self.assertEqual(result, [1, 2, 2, 3, 3, 4])


class TestCountWordOccurrences(unittest.TestCase):
    """Tests for the count_word_occurrences function."""
    
    def test_count_word_occurrences_normal(self):
        """Test counting word occurrences normally."""
        text = "The cat sat on the cat mat"
        count = count_word_occurrences(text, "cat")
        self.assertEqual(count, 2)
    
    def test_count_word_occurrences_case_sensitive(self):
        """Test that word matching is case-insensitive."""
        text = "The Cat sat on the cat mat"
        count = count_word_occurrences(text, "cat")
        # BUG: Current implementation is case-sensitive
        self.assertEqual(count, 2)
    
    def test_count_word_occurrences_partial_match(self):
        """Test that partial matches are not counted."""
        text = "The category catalog has cats and a cat"
        count = count_word_occurrences(text, "cat")
        # Should only count exact word "cat", not 'category', 'catalog', or 'cats'
        self.assertEqual(count, 1)
    
    def test_count_word_occurrences_empty(self):
        """Test counting in empty text."""
        count = count_word_occurrences("", "cat")
        self.assertEqual(count, 0)


if __name__ == '__main__':
    unittest.main()
