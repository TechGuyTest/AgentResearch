"""
Unit Tests for String Utilities Module

These tests expose bugs in the string_utils.py module.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice.string_utils import (
    reverse_string, count_vowels, is_palindrome,
    capitalize_words, remove_duplicates, find_longest_word, truncate
)


class TestReverseString(unittest.TestCase):
    """Tests for the reverse_string function."""
    
    def test_reverse_normal_string(self):
        """Test reversing a normal string."""
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_string(""), "")
    
    def test_reverse_single_char(self):
        """Test reversing a single character."""
        self.assertEqual(reverse_string("a"), "a")


class TestCountVowels(unittest.TestCase):
    """Tests for the count_vowels function."""
    
    def test_count_vowels_lowercase(self):
        """Test counting lowercase vowels."""
        self.assertEqual(count_vowels("hello"), 2)
    
    def test_count_vowels_uppercase(self):
        """Test counting uppercase vowels - should count them too."""
        self.assertEqual(count_vowels("HELLO"), 2)  # BUG: Currently returns 0
    
    def test_count_vowels_mixed_case(self):
        """Test counting vowels in mixed case string."""
        self.assertEqual(count_vowels("HeLLo WoRLd"), 3)  # BUG: Currently returns 1 or 2
    
    def test_count_vowels_no_vowels(self):
        """Test counting vowels in string with no vowels."""
        self.assertEqual(count_vowels("bcdfg"), 0)


class TestIsPalindrome(unittest.TestCase):
    """Tests for the is_palindrome function."""
    
    def test_is_palindrome_simple(self):
        """Test simple palindrome."""
        self.assertTrue(is_palindrome("radar"))
    
    def test_is_palindrome_not(self):
        """Test non-palindrome."""
        self.assertFalse(is_palindrome("hello"))
    
    def test_is_palindrome_case_insensitive(self):
        """Test palindrome with mixed case - should be case insensitive."""
        self.assertTrue(is_palindrome("Radar"))  # BUG: Currently returns False
    
    def test_is_palindrome_with_spaces(self):
        """Test palindrome with spaces - should ignore spaces."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))  # BUG: Currently returns False


class TestCapitalizeWords(unittest.TestCase):
    """Tests for the capitalize_words function."""
    
    def test_capitalize_words_normal(self):
        """Test capitalizing normal words."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
    
    def test_capitalize_words_empty(self):
        """Test capitalizing empty string."""
        self.assertEqual(capitalize_words(""), "")
    
    def test_capitalize_words_single(self):
        """Test capitalizing single word."""
        self.assertEqual(capitalize_words("hello"), "Hello")


class TestRemoveDuplicates(unittest.TestCase):
    """Tests for the remove_duplicates function."""
    
    def test_remove_duplicates_normal(self):
        """Test removing duplicates from normal string."""
        self.assertEqual(remove_duplicates("hello"), "helo")
    
    def test_remove_duplicates_no_duplicates(self):
        """Test string with no duplicates."""
        self.assertEqual(remove_duplicates("abc"), "abc")
    
    def test_remove_duplicates_all_same(self):
        """Test string with all same characters."""
        self.assertEqual(remove_duplicates("aaaa"), "a")


class TestFindLongestWord(unittest.TestCase):
    """Tests for the find_longest_word function."""
    
    def test_find_longest_word_normal(self):
        """Test finding longest word in normal string."""
        self.assertEqual(find_longest_word("The quick brown fox"), "quick")
    
    def test_find_longest_word_empty(self):
        """Test finding longest word in empty string."""
        self.assertEqual(find_longest_word(""), "")
    
    def test_find_longest_word_single(self):
        """Test finding longest word in single word string."""
        self.assertEqual(find_longest_word("hello"), "hello")


class TestTruncate(unittest.TestCase):
    """Tests for the truncate function."""
    
    def test_truncate_no_truncation_needed(self):
        """Test truncate when no truncation needed."""
        self.assertEqual(truncate("hello", 10), "hello")
    
    def test_truncate_exact_length(self):
        """Test truncate at exact length."""
        self.assertEqual(truncate("hello", 5), "hello")
    
    def test_truncate_with_ellipsis(self):
        """Test truncate with ellipsis - total length should not exceed max_length."""
        result = truncate("hello world", 8)
        # BUG: Current implementation returns "hello..." which is 8 chars but ellipsis should be included in max
        self.assertEqual(len(result), 8)
        self.assertTrue(result.endswith("..."))
    
    def test_truncate_short_max_length(self):
        """Test truncate with very short max length."""
        result = truncate("hello", 5)
        # When max_length <= 3, ellipsis takes all space
        self.assertLessEqual(len(result), 5)


if __name__ == '__main__':
    unittest.main()
