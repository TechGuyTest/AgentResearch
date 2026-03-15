"""
Unit Tests for Debug Challenge Module

These tests verify the fixes in debug_challenge.py.
"""

import unittest
import sys
import os
import tempfile

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice.debug_challenge import (
    calculate_average, find_maximum, process_user_data,
    parse_config_file, validate_email
)


class TestCalculateAverage(unittest.TestCase):
    """Tests for calculate_average."""
    
    def test_calculate_average_normal(self):
        """Test calculating average of normal list."""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    
    def test_calculate_average_empty(self):
        """Test calculating average of empty list - should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_average([])
    
    def test_calculate_average_single(self):
        """Test calculating average of single element."""
        self.assertEqual(calculate_average([42]), 42.0)


class TestFindMaximum(unittest.TestCase):
    """Tests for find_maximum."""
    
    def test_find_maximum_normal(self):
        """Test finding maximum in normal list."""
        self.assertEqual(find_maximum([3, 7, 2, 9, 1]), 9)
    
    def test_find_maximum_negative(self):
        """Test finding maximum in negative numbers."""
        self.assertEqual(find_maximum([-5, -2, -10, -1]), -1)
    
    def test_find_maximum_empty(self):
        """Test finding maximum in empty list."""
        self.assertIsNone(find_maximum([]))
    
    def test_find_maximum_single(self):
        """Test finding maximum in single element list."""
        self.assertEqual(find_maximum([42]), 42)


class TestProcessUserData(unittest.TestCase):
    """Tests for process_user_data."""
    
    def test_process_user_data_normal(self):
        """Test processing normal user data."""
        users = [
            {'id': 1, 'name': 'Alice', 'active': True, 'scores': [85, 90, 78]},
            {'id': 2, 'name': 'Bob', 'active': False, 'scores': [92, 88]},
            {'id': 3, 'name': 'Charlie', 'active': True, 'scores': []},
        ]
        result = process_user_data(users)
        
        # Only active users should be included
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'Alice')
        self.assertEqual(result[1]['name'], 'Charlie')
    
    def test_process_user_data_with_invalid_type(self):
        """Test processing with non-dict items - should skip them."""
        users = [
            {'id': 1, 'name': 'Alice', 'active': True, 'scores': [85, 90]},
            "invalid",
            None,
            {'id': 2, 'name': 'Bob', 'active': True, 'scores': [92]},
        ]
        result = process_user_data(users)
        
        # Only valid dict users should be included
        self.assertEqual(len(result), 2)
    
    def test_process_user_data_empty_scores(self):
        """Test processing user with empty scores."""
        users = [
            {'id': 1, 'name': 'Alice', 'active': True, 'scores': []},
        ]
        result = process_user_data(users)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['average'], 0)
        self.assertEqual(result[0]['total'], 0)


class TestParseConfigFile(unittest.TestCase):
    """Tests for parse_config_file."""
    
    def test_parse_config_file_valid(self):
        """Test parsing valid config file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as f:
            f.write("# Comment\n")
            f.write("key1=value1\n")
            f.write("key2 = value2\n")
            temp_path = f.name
        
        try:
            config = parse_config_file(temp_path)
            self.assertEqual(config['key1'], 'value1')
            self.assertEqual(config['key2'], 'value2')
        finally:
            os.unlink(temp_path)
    
    def test_parse_config_file_not_found(self):
        """Test parsing non-existent file."""
        with self.assertRaises(FileNotFoundError):
            parse_config_file('/nonexistent/path/config.conf')


class TestValidateEmail(unittest.TestCase):
    """Tests for validate_email."""
    
    def test_validate_email_valid(self):
        """Test validating valid email."""
        self.assertTrue(validate_email("test@example.com"))
    
    def test_validate_email_invalid_no_at(self):
        """Test validating email without @."""
        self.assertFalse(validate_email("invalid"))
    
    def test_validate_email_invalid_no_domain(self):
        """Test validating email with empty domain."""
        self.assertFalse(validate_email("user@"))
    
    def test_validate_email_invalid_no_local(self):
        """Test validating email with empty local part."""
        self.assertFalse(validate_email("@domain.com"))
    
    def test_validate_email_invalid_no_dot_in_domain(self):
        """Test validating email without dot in domain."""
        self.assertFalse(validate_email("user@domain"))
    
    def test_validate_email_empty(self):
        """Test validating empty string."""
        self.assertFalse(validate_email(""))
    
    def test_validate_email_none(self):
        """Test validating None."""
        self.assertFalse(validate_email(None))


if __name__ == '__main__':
    unittest.main()
