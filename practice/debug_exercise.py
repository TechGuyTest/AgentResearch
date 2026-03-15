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
    # Fixed Problem 1: Handle empty list
    if not users or len(users) == 0:
        return {
            'user_count': 0,
            'average_score': 0,
            'average_age': 0,
            'score_range': 0,
            'max_score': 0,
            'min_score': 0,
            'valid_users': 0
        }
    
    total_score = 0
    total_age = 0
    valid_users = 0
    scores = []
    
    # Fixed Problem 2: Start at 0 instead of 1 to include all users
    for i in range(0, len(users)):
        user = users[i]
        
        # Fixed Problem 3: Check for missing fields and None values
        if 'score' not in user or 'age' not in user:
            continue
        
        score = user['score']
        age = user['age']
        
        # Validate types
        if not isinstance(score, (int, float)) or not isinstance(age, (int, float)):
            continue
        
        total_score += score
        total_age += age
        valid_users += 1
        scores.append(score)
    
    # Fixed Problem 4: Handle division by zero
    if valid_users == 0:
        return {
            'user_count': len(users),
            'average_score': 0,
            'average_age': 0,
            'score_range': 0,
            'max_score': 0,
            'min_score': 0,
            'valid_users': 0
        }
    
    average_score = total_score / valid_users
    average_age = total_age / valid_users
    
    # Fixed Problem 5: Calculate max/min in the same loop (already done above)
    max_score = max(scores) if scores else 0
    min_score = min(scores) if scores else 0
    
    # Fixed Problem 6: Return all calculated values
    return {
        'user_count': len(users),
        'average_score': average_score,
        'average_age': average_age,
        'score_range': max_score - min_score,
        'max_score': max_score,
        'min_score': min_score,
        'valid_users': valid_users
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
    # Fixed Problem 7: Validate threshold type
    if not isinstance(threshold, (int, float)):
        return []
    
    active = []
    
    for user in users:
        # Fixed Problem 8: Check if score exists before comparing
        if 'score' not in user:
            continue
        
        score = user['score']
        if not isinstance(score, (int, float)):
            continue
        
        if score >= threshold:
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
    # Fixed Problem 9: Validate count parameter
    if not isinstance(count, int) or count < 0:
        return []
    
    # Filter users with valid scores
    valid_users = [u for u in users if 'score' in u and isinstance(u['score'], (int, float))]
    
    # Sort by score descending
    sorted_users = sorted(valid_users, key=lambda x: x['score'], reverse=True)
    
    # Fixed Problem 10: Bounds checking on count (Python slicing handles this, but explicit is better)
    return sorted_users[:count]


def validate_user_data(user):
    """
    Validate user data structure.
    
    Args:
        user: User dictionary
    
    Returns:
        Boolean indicating if valid
    """
    # Fixed Problem 11: Complete validation with type and range checks
    required_fields = ['name', 'age', 'score']
    
    # Check all required fields exist
    for field in required_fields:
        if field not in user:
            return False
    
    # Validate name is a string
    if not isinstance(user['name'], str) or not user['name'].strip():
        return False
    
    # Validate age is a number and in reasonable range
    if not isinstance(user['age'], (int, float)):
        return False
    if user['age'] < 0 or user['age'] > 150:
        return False
    
    # Validate score is a number and in reasonable range (0-100)
    if not isinstance(user['score'], (int, float)):
        return False
    if user['score'] < 0 or user['score'] > 100:
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
    print(f"  Max score: {stats['max_score']}")
    print(f"  Min score: {stats['min_score']}")
    
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
