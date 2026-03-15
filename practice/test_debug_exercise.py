"""
Unit Tests for Debug Exercise Module

These tests expose bugs in the debug_exercise.py module.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice.debug_exercise import (
    calculate_user_stats, filter_active_users, get_top_performers, validate_user_data
)


class TestCalculateUserStats(unittest.TestCase):
    """Tests for the calculate_user_stats function."""
    
    def test_empty_list(self):
        """Test calculating stats for empty list - should handle gracefully."""
        # BUG: Current implementation raises division by zero
        result = calculate_user_stats([])
        self.assertEqual(result['user_count'], 0)
        self.assertEqual(result['average_score'], 0)
        self.assertEqual(result['average_age'], 0)
    
    def test_single_user(self):
        """Test calculating stats for single user."""
        users = [{'name': 'Alice', 'age': 25, 'score': 85}]
        result = calculate_user_stats(users)
        self.assertEqual(result['user_count'], 1)
        self.assertEqual(result['average_score'], 85)
        self.assertEqual(result['average_age'], 25)
    
    def test_multiple_users(self):
        """Test calculating stats for multiple users - BUG: Loop starts at 1, skipping first user."""
        users = [
            {'name': 'Alice', 'age': 25, 'score': 85},
            {'name': 'Bob', 'age': 30, 'score': 92},
            {'name': 'Charlie', 'age': 28, 'score': 78},
        ]
        result = calculate_user_stats(users)
        # Should include all 3 users: (85+92+78)/3 = 85.0
        self.assertEqual(result['average_score'], 85.0)
        self.assertEqual(result['average_age'], 27.666666666666668)  # (25+30+28)/3
    
    def test_user_missing_age_field(self):
        """Test handling user with missing age field - BUG: No None/missing field check."""
        users = [
            {'name': 'Alice', 'age': 25, 'score': 85},
            {'name': 'Eve', 'score': 88},  # Missing age
        ]
        # Should handle gracefully, either skip or use default
        result = calculate_user_stats(users)
        self.assertIsNotNone(result)
    
    def test_returns_all_fields(self):
        """Test that result includes all calculated fields - BUG: Missing max_score, min_score."""
        users = [
            {'name': 'Alice', 'age': 25, 'score': 85},
            {'name': 'Bob', 'age': 30, 'score': 92},
        ]
        result = calculate_user_stats(users)
        # BUG: Current implementation doesn't return max_score and min_score
        self.assertIn('max_score', result)
        self.assertIn('min_score', result)
        self.assertEqual(result['max_score'], 92)
        self.assertEqual(result['min_score'], 85)


class TestFilterActiveUsers(unittest.TestCase):
    """Tests for the filter_active_users function."""
    
    def test_normal_filtering(self):
        """Test filtering active users normally."""
        users = [
            {'name': 'Alice', 'age': 25, 'score': 85},
            {'name': 'Bob', 'age': 30, 'score': 45},
            {'name': 'Charlie', 'age': 28, 'score': 78},
        ]
        result = filter_active_users(users, 80)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Alice')
    
    def test_invalid_threshold_type(self):
        """Test filtering with invalid threshold type - BUG: No type validation."""
        users = [{'name': 'Alice', 'age': 25, 'score': 85}]
        # Should handle invalid threshold gracefully
        result = filter_active_users(users, "invalid")
        self.assertIsNotNone(result)
    
    def test_user_missing_score_field(self):
        """Test handling user with missing score field - BUG: No field existence check."""
        users = [
            {'name': 'Alice', 'age': 25, 'score': 85},
            {'name': 'Eve', 'age': 22},  # Missing score
        ]
        # Should handle gracefully
        result = filter_active_users(users, 80)
        self.assertIsNotNone(result)


class TestGetTopPerformers(unittest.TestCase):
    """Tests for the get_top_performers function."""
    
    def test_normal_top_performers(self):
        """Test getting top performers normally."""
        users = [
            {'name': 'Alice', 'age': 25, 'score': 85},
            {'name': 'Bob', 'age': 30, 'score': 92},
            {'name': 'Charlie', 'age': 28, 'score': 78},
        ]
        result = get_top_performers(users, 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'Bob')  # Highest score
        self.assertEqual(result[1]['name'], 'Alice')
    
    def test_count_larger_than_list(self):
        """Test getting more performers than available - BUG: No bounds checking."""
        users = [
            {'name': 'Alice', 'age': 25, 'score': 85},
        ]
        # Should return all available users without error
        result = get_top_performers(users, 10)
        self.assertEqual(len(result), 1)
    
    def test_negative_count(self):
        """Test getting negative count - BUG: No validation."""
        users = [{'name': 'Alice', 'age': 25, 'score': 85}]
        result = get_top_performers(users, -1)
        self.assertEqual(len(result), 0)  # Should return empty list


class TestValidateUserData(unittest.TestCase):
    """Tests for the validate_user_data function."""
    
    def test_valid_user(self):
        """Test validating valid user data."""
        user = {'name': 'Alice', 'age': 25, 'score': 85}
        self.assertTrue(validate_user_data(user))
    
    def test_missing_field(self):
        """Test validating user with missing field."""
        user = {'name': 'Alice', 'score': 85}  # Missing age
        self.assertFalse(validate_user_data(user))
    
    def test_invalid_age_type(self):
        """Test validating user with invalid age type - BUG: No type checking."""
        user = {'name': 'Alice', 'age': 'twenty-five', 'score': 85}
        self.assertFalse(validate_user_data(user))
    
    def test_negative_age(self):
        """Test validating user with negative age - BUG: No range validation."""
        user = {'name': 'Alice', 'age': -5, 'score': 85}
        self.assertFalse(validate_user_data(user))
    
    def test_score_out_of_range(self):
        """Test validating user with score out of range - BUG: No range validation."""
        user = {'name': 'Alice', 'age': 25, 'score': 150}  # Score > 100
        self.assertFalse(validate_user_data(user))


if __name__ == '__main__':
    unittest.main()
