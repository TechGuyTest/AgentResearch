"""
Debug Challenge Exercise
========================
This file contains intentional bugs and code smells for debugging practice.
Find and fix all the issues!

Hint: There are 5 problems hidden in this code.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    FIX 1: Handle empty list boundary case
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_maximum(items):
    """
    Find the maximum value in a list.
    
    FIX 2: Correct comparison operator to find maximum
    """
    if not items:
        return None
    
    max_value = items[0]
    for item in items[1:]:
        if item > max_value:
            max_value = item
    
    return max_value


def process_user_data(users):
    """
    Process user data and return active users with their scores.
    
    FIX 3 & 4: Add type checking and optimize score processing
    """
    result = []
    
    for user in users:
        # FIX 4: Add type check - user should be a dictionary
        if not isinstance(user, dict):
            continue
        
        user_id = user.get('id')
        user_name = user.get('name')
        is_active = user.get('active', False)
        
        if is_active:
            # FIX 3: Optimize score processing with list comprehension
            scores = [score for score in user.get('scores', []) if score > 0]
            
            # Calculate sum once and reuse
            total_score = sum(scores)
            average_score = total_score / len(scores) if scores else 0
            
            result.append({
                'id': user_id,
                'name': user_name,
                'average': average_score,
                'total': total_score
            })
    
    return result


def parse_config_file(filepath):
    """
    Parse a configuration file and return settings as a dictionary.
    
    FIX 5: Use context manager to ensure file is properly closed
    """
    config = {}
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
    
    return config


def validate_email(email):
    """
    Simple email validation.
    
    FIX: Improved validation to handle edge cases
    """
    if not email or not isinstance(email, str):
        return False
    
    # Check for basic structure: something@something.something
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local, domain = parts
    
    # Local part should not be empty
    if not local:
        return False
    
    # Domain should contain at least one dot and not start/end with it
    if not domain or '.' not in domain:
        return False
    
    if domain.startswith('.') or domain.endswith('.'):
        return False
    
    return True


# Test data for practice
if __name__ == "__main__":
    # Test calculate_average
    print("Testing calculate_average:")
    print(calculate_average([1, 2, 3, 4, 5]))  # Should be 3.0
    # print(calculate_average([]))  # Uncomment to see the bug!
    
    # Test find_maximum
    print("\nTesting find_maximum:")
    print(find_maximum([3, 7, 2, 9, 1]))  # Should be 9, but will return 1!
    
    # Test process_user_data
    print("\nTesting process_user_data:")
    users = [
        {'id': 1, 'name': 'Alice', 'active': True, 'scores': [85, 90, 78]},
        {'id': 2, 'name': 'Bob', 'active': False, 'scores': [92, 88]},
        {'id': 3, 'name': 'Charlie', 'active': True, 'scores': []},
    ]
    print(process_user_data(users))
    
    # Test validate_email
    print("\nTesting validate_email:")
    print(validate_email("test@example.com"))  # True
    print(validate_email("invalid"))  # False
    print(validate_email("user@"))  # Should be False but returns True!
