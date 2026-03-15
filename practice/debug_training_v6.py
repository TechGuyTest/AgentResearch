#!/usr/bin/env python3
"""
Debug Training Exercise v6
==========================
This file contains intentional bugs and code smells for debugging practice.
Find and fix the issues!

Issues to find:
- Logic errors
- Unhandled edge cases
- Inefficient patterns
- Missing error handling
"""


# ============================================================================
# Problem 1: Logic Error in Calculation
# ============================================================================
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    BUG: The discount calculation is incorrect.
    HINT: Check the math operation - should we multiply or divide?
    """
    # TODO: Fix the discount calculation
    discount_amount = price / discount_percent  # BUG: Wrong operator
    final_price = price - discount_amount
    return final_price


# ============================================================================
# Problem 2: Unhandled Edge Cases
# ============================================================================
def find_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    BUG: No handling for empty list - will cause ZeroDivisionError
    HINT: What happens when numbers is []?
    """
    # TODO: Add check for empty list
    total = sum(numbers)
    average = total / len(numbers)  # BUG: Crashes on empty list
    return average


# ============================================================================
# Problem 3: Inefficient Pattern - O(n²) instead of O(n)
# ============================================================================
def find_duplicates(items):
    """
    Find duplicate items in a list.
    
    BUG: Uses nested loops - very inefficient for large lists.
    HINT: Could use a set or Counter for O(n) solution.
    """
    duplicates = []
    # TODO: Optimize this to O(n) using a set
    for i in range(len(items)):  # BUG: O(n²) complexity
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


# ============================================================================
# Problem 4: Mutable Default Argument
# ============================================================================
def add_item_to_inventory(item, inventory={}):
    """
    Add an item to the inventory dictionary.
    
    BUG: Using mutable default argument - causes shared state between calls.
    HINT: What happens when you call this function multiple times without 
          passing inventory? The default dict is created once at function 
          definition time, not each call!
    """
    # TODO: Fix the mutable default argument issue
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1
    return inventory


# ============================================================================
# Problem 5: Missing Error Handling
# ============================================================================
def read_config_value(config, key):
    """
    Read a configuration value and convert to integer.
    
    BUG: No error handling for missing keys or invalid values.
    HINT: What if key doesn't exist? What if value isn't convertible to int?
    """
    # TODO: Add try-except for KeyError and ValueError
    value = config[key]  # BUG: KeyError if key missing
    return int(value)  # BUG: ValueError if not convertible


# ============================================================================
# Test Cases (for verification after fixes)
# ============================================================================
if __name__ == "__main__":
    print("Testing calculate_discount...")
    # Expected: 100 * 0.2 = 20 discount, final = 80
    print(f"  100 with 20% discount = {calculate_discount(100, 20)}")
    
    print("\nTesting find_average...")
    # Expected: Should handle empty list gracefully
    print(f"  Average of [1,2,3,4,5] = {find_average([1, 2, 3, 4, 5])}")
    # print(f"  Average of [] = {find_average([])}")  # Will crash!
    
    print("\nTesting find_duplicates...")
    # Expected: [2, 3]
    print(f"  Duplicates in [1,2,2,3,3,4] = {find_duplicates([1, 2, 2, 3, 3, 4])}")
    
    print("\nTesting add_item_to_inventory...")
    # Expected: Each call should start fresh if no inventory passed
    inv1 = add_item_to_inventory("apple")
    inv2 = add_item_to_inventory("banana")
    print(f"  Inventory 1: {inv1}")
    print(f"  Inventory 2: {inv2}")  # BUG: Will contain both items!
    
    print("\nTesting read_config_value...")
    config = {"port": "8080", "timeout": "30"}
    print(f"  Port value = {read_config_value(config, 'port')}")
    # print(f"  Missing key = {read_config_value(config, 'missing')}")  # Will crash!
