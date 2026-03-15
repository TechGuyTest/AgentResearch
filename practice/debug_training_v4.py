"""
Debug Training Exercise V4
==========================
This file contains intentional bugs and code smells for debugging practice.
Find and fix all the issues!

Problem areas are marked with FIXME/TODO comments.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    FIXME: What happens if the list is empty?
    FIXME: Should we validate that all items are numbers?
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_maximum(values):
    """
    Find the maximum value in a list.
    
    FIXME: This has a logic error - check the comparison operator!
    FIXME: What if values is None or empty?
    """
    if not values:
        return None
    
    max_val = values[0]
    for val in values:
        if val < max_val:  # BUG: Wrong comparison operator
            max_val = val
    return max_val


def process_user_data(users):
    """
    Process user data and return active users with their scores.
    
    FIXME: Inefficient - creates unnecessary intermediate lists
    FIXME: Doesn't handle missing 'score' key
    FIXME: Mutable default argument issue
    """
    result = []  # Good: not using mutable default
    active_users = []
    
    # First pass: filter active users
    for user in users:
        if user.get('active', False):
            active_users.append(user)
    
    # Second pass: extract scores (inefficient - should be one pass)
    for user in active_users:
        score = user['score']  # BUG: What if 'score' key doesn't exist?
        result.append({
            'name': user['name'],
            'score': score
        })
    
    return result


def search_item(items, target):
    """
    Search for an item in a list and return its index.
    
    FIXME: Inefficient O(n²) pattern - why are we iterating twice?
    FIXME: Returns -1 but also prints - inconsistent behavior
    """
    # First loop: check if item exists
    found = False
    for item in items:
        if item == target:
            found = True
            break
    
    # Second loop: find the index (unnecessary!)
    if found:
        for i, item in enumerate(items):
            if item == target:
                return i
    
    print(f"Item {target} not found")
    return -1


def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying discount.
    
    FIXME: No validation for negative prices or discounts > 100
    FIXME: Floating point precision issues not handled
    FIXME: Discount percent should be validated (0-100 range)
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price


def merge_and_sort_lists(list1, list2):
    """
    Merge two lists and return sorted result.
    
    FIXME: Modifies input lists - side effect!
    FIXME: Inefficient sorting approach
    """
    # BUG: This modifies the original list1!
    list1.extend(list2)
    
    # Inefficient: bubble sort instead of built-in sort
    result = list1
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result


# ============== Test Cases ==============
if __name__ == "__main__":
    print("=== Testing calculate_average ===")
    print(calculate_average([1, 2, 3, 4, 5]))  # Expected: 3.0
    # print(calculate_average([]))  # What happens here?
    
    print("\n=== Testing find_maximum ===")
    print(find_maximum([3, 7, 2, 9, 1]))  # Expected: 9
    print(find_maximum([]))  # Expected: None
    
    print("\n=== Testing process_user_data ===")
    users = [
        {'name': 'Alice', 'active': True, 'score': 95},
        {'name': 'Bob', 'active': False, 'score': 80},
        {'name': 'Charlie', 'active': True, 'score': 88},
        {'name': 'Diana', 'active': True}  # Missing score!
    ]
    print(process_user_data(users))
    
    print("\n=== Testing search_item ===")
    items = ['apple', 'banana', 'cherry', 'date']
    print(search_item(items, 'cherry'))  # Expected: 2
    print(search_item(items, 'grape'))   # Expected: -1
    
    print("\n=== Testing calculate_discount ===")
    print(calculate_discount(100, 20))  # Expected: 80.0
    print(calculate_discount(100, 150))  # What happens with >100% discount?
    print(calculate_discount(-50, 10))   # What about negative price?
    
    print("\n=== Testing merge_and_sort_lists ===")
    list_a = [5, 2, 8]
    list_b = [1, 9, 3]
    print(f"Before: list_a = {list_a}")
    result = merge_and_sort_lists(list_a, list_b)
    print(f"After: list_a = {list_a}")  # Original list modified!
    print(f"Result: {result}")
