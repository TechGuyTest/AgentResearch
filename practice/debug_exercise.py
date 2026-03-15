"""
Debug Practice Exercise
========================
This file contains intentional bugs and code smells for debugging practice.
Find and fix the issues!

Issues to find:
- Logic errors
- Unhandled edge cases
- Inefficient patterns
- Potential security issues
"""


# Issue 1: Logic Error - Off-by-one in loop
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    BUG: Off-by-one error in loop range
    """
    if not numbers:
        return 0
    
    total = 0
    # TODO: Check the loop range - is it iterating correctly?
    for i in range(1, len(numbers)):  # Hint: Should start from 0?
        total += numbers[i]
    
    return total / len(numbers)


# Issue 2: Unhandled Edge Case - Division by zero
def safe_divide(a, b):
    """
    Safely divide two numbers.
    BUG: Doesn't handle division by zero properly
    """
    # TODO: What happens when b is 0?
    result = a / b
    return result


# Issue 3: Inefficient Pattern - O(n²) when O(n) is possible
def find_duplicates(items):
    """
    Find duplicate items in a list.
    BUG: Uses nested loops instead of a set
    """
    duplicates = []
    # TODO: This is O(n²) - can you make it O(n)?
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    
    return duplicates


# Issue 4: Mutable Default Argument - Classic Python gotcha
def add_item(item, collection=[]):
    """
    Add an item to a collection.
    BUG: Mutable default argument causes unexpected behavior
    """
    # TODO: What happens when calling this function multiple times without 
    # providing the collection argument?
    collection.append(item)
    return collection


# Issue 5: Unvalidated Input - Security/Robustness issue
def process_user_data(user_input):
    """
    Process user input data.
    BUG: No input validation or sanitization
    """
    # TODO: What if user_input is None, empty, or malicious?
    data = user_input.strip()
    processed = eval(data)  # Warning: eval is dangerous!
    return processed * 2


# Helper function for testing
def run_tests():
    """Run basic tests on the functions above."""
    print("Testing calculate_average...")
    print(f"  [1, 2, 3, 4, 5] average: {calculate_average([1, 2, 3, 4, 5])}")
    print(f"  Empty list average: {calculate_average([])}")
    
    print("\nTesting safe_divide...")
    print(f"  10 / 2 = {safe_divide(10, 2)}")
    print(f"  10 / 0 = {safe_divide(10, 0)}")
    
    print("\nTesting find_duplicates...")
    print(f"  [1, 2, 2, 3, 3, 3]: {find_duplicates([1, 2, 2, 3, 3, 3])}")
    
    print("\nTesting add_item...")
    print(f"  First call: {add_item('a')}")
    print(f"  Second call: {add_item('b')}")
    print(f"  Third call with new list: {add_item('c', [])}")
    
    print("\nTesting process_user_data...")
    print(f"  '5' processed: {process_user_data('5')}")
    # Try: process_user_data('__import__("os").system("ls")')


if __name__ == "__main__":
    run_tests()
