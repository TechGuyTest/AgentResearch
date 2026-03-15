#!/usr/bin/env python3
"""
Debug Practice Exercise: User Data Analyzer
Contains several intentional bugs for debugging practice.
Try to find and fix all issues!

Problems to look for:
1. Logic error in average calculation
2. Off-by-one error in loop
3. Missing edge case handling (empty input, None values)
4. Inefficient pattern (repeated computation)
5. Type error potential
6. Missing validation
"""

def calculate_user_stats(users):
    """
    Calculate statistics for a list of user objects.
    
    Args:
        users: List of dictionaries with 'name', 'age', 'score' keys
    
    Returns:
        Dictionary with statistics
    """
    # Problem 1: No validation for empty list
    total_score = 0
    total_age = 0
    valid_users = 0
    
    # Problem 2: Off-by-one error - should iterate through all users
    for i in range(1, len(users)):  # BUG: starts at 1 instead of 0
        user = users[i]
        
        # Problem 3: No None check
        total_score += user['score']
        total_age += user['age']
        valid_users += 1
    
    # Problem 4: Division by zero risk if no valid users
    average_score = total_score / valid_users
    average_age = total_age / valid_users
    
    # Problem 5: Inefficient - recalculating max/min in separate loops
    max_score = 0
    min_score = 999999
    for user in users:
        if user['score'] > max_score:
            max_score = user['score']
        if user['score'] < min_score:
            min_score = user['score']
    
    # Problem 6: Missing return of some calculated values
    return {
        'user_count': len(users),
        'average_score': average_score,
        'average_age': average_age,
        'score_range': max_score - min_score
        # Missing: max_score, min_score, valid_users count
    }


def filter_active_users(users, threshold=50):
    """
    Filter users with score above threshold.
    
    Args:
        users: List of user dictionaries
        threshold: Minimum score to be considered active
    
    Returns:
        List of active users
    """
    active = []
    
    # Problem 7: No validation on threshold type
    for user in users:
        # Problem 8: Direct comparison without checking if score exists
        if user['score'] >= threshold:
            active.append(user)
    
    return active


def get_top_performers(users, count=3):
    """
    Get top N performers by score.
    
    Args:
        users: List of user dictionaries
        count: Number of top performers to return
    
    Returns:
        List of top performers
    """
    # Problem 9: Inefficient sorting - sorts entire list when only need top N
    sorted_users = sorted(users, key=lambda x: x['score'], reverse=True)
    
    # Problem 10: No bounds checking on count
    return sorted_users[:count]


def validate_user_data(user):
    """
    Validate user data structure.
    
    Args:
        user: User dictionary
    
    Returns:
        Boolean indicating if valid
    """
    # Problem 11: Incomplete validation - doesn't check value types or ranges
    required_fields = ['name', 'age', 'score']
    
    for field in required_fields:
        if field not in user:
            return False
    
    return True


# Test data with some edge cases
test_users = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 30, 'score': 92},
    {'name': 'Charlie', 'age': 28, 'score': 78},
    {'name': 'Diana', 'age': 35, 'score': 95},
    # Edge case: missing fields
    {'name': 'Eve', 'score': 88},  # Missing age
    # Edge case: invalid values
    {'name': 'Frank', 'age': -5, 'score': 150},  # Invalid age and score
]

if __name__ == '__main__':
    print("Testing User Data Analyzer...")
    print("\n1. Calculating stats:")
    stats = calculate_user_stats(test_users)
    print(f"  User count: {stats['user_count']}")
    print(f"  Average score: {stats['average_score']:.2f}")
    print(f"  Average age: {stats['average_age']:.2f}")
    print(f"  Score range: {stats['score_range']}")
    
    print("\n2. Filtering active users (threshold=80):")
    active = filter_active_users(test_users, 80)
    print(f"  Found {len(active)} active users")
    for user in active:
        print(f"    - {user['name']}: {user['score']}")
    
    print("\n3. Top 2 performers:")
    top = get_top_performers(test_users, 2)
    for i, user in enumerate(top, 1):
        print(f"    {i}. {user['name']} - Score: {user['score']}")
    
    print("\n4. Validating users:")
    for user in test_users:
        is_valid = validate_user_data(user)
        status = "✓" if is_valid else "✗"
        print(f"  {status} {user.get('name', 'Unknown')}")
