"""
Practice Exercise: Data Structure Utilities

This module contains data structure manipulation functions with intentional bugs.
"""


def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_min(numbers):
    """Find the minimum number in a list."""
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def binary_search(sorted_list, target):
    """Perform binary search on a sorted list."""
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def merge_dicts(dict1, dict2):
    """Merge two dictionaries."""
    result = dict1.copy()
    result.update(dict2)
    return result


def flatten_list(nested_list):
    """Flatten a nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def remove_element(lst, element):
    """Remove all occurrences of an element from a list."""
    # Create a new list without the element (doesn't modify original)
    return [item for item in lst if item != element]


def count_occurrences(lst, element):
    """Count occurrences of an element in a list."""
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
