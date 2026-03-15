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
    
    BUG 1: Boundary case not handled - what if numbers is empty?
    """
    total = 0
    for num in numbers:
        total += num
    # TODO: Check for division by zero when numbers is empty
    return total / len(numbers)


def find_maximum(items):
    """
    Find the maximum value in a list.
    
    BUG 2: Logic error - comparison operator is wrong
    """
    if not items:
        return None
    
    max_value = items[0]
    for item in items[1:]:
        # TODO: This comparison is incorrect - should find maximum, not minimum
        if item < max_value:
            max_value = item
    
    return max_value


def process_user_data(users):
    """
    Process user data and return active users with their scores.
    
    BUG 3: Inefficient pattern - nested loops could be optimized
    BUG 4: Missing type checking - what if user is not a dict?
    """
    result = []
    
    for user in users:
        # TODO: Add type check - user should be a dictionary
        user_id = user['id']
        user_name = user['name']
        is_active = user['active']
        
        if is_active:
            # Inefficient: Creating a new list and searching every time
            scores = []
            for score in user.get('scores', []):
                if score > 0:
                    scores.append(score)
            
            # TODO: This calculation is repeated unnecessarily
            average_score = sum(scores) / len(scores) if scores else 0
            total_score = sum(scores)
            
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
    
    BUG 5: Resource leak - file not properly closed in all cases
    """
    config = {}
    
    # TODO: File should be opened with context manager (with statement)
    f = open(filepath, 'r')
    
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    
    # TODO: File might not be closed if an exception occurs above
    f.close()
    
    return config


def validate_email(email):
    """
    Simple email validation.
    
    Additional issue: This validation is too simplistic and 
    will accept invalid emails.
    """
    # TODO: This is a very basic check - missing many edge cases
    # e.g., "user@" or "@domain.com" or "user@domain" would pass/fail incorrectly
    if '@' in email and '.' in email:
        return True
    return False


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
