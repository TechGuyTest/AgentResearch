"""
Practice Exercise: String Utilities

This module contains string manipulation functions with intentional bugs.
"""


def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


def count_vowels(s):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def is_palindrome(s):
    """Check if a string is a palindrome."""
    # Remove spaces and convert to lowercase for comparison
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_words(s):
    """Capitalize first letter of each word."""
    words = s.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return " ".join(result)


def remove_duplicates(s):
    """Remove duplicate characters from a string."""
    seen = []
    result = ""
    for char in s:
        if char not in seen:
            seen.append(char)
            result += char
    return result


def find_longest_word(s):
    """Find the longest word in a string."""
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):  # BUG: Doesn't handle tie-breaking consistently
            longest = word
    return longest


def truncate(s, max_length):
    """Truncate string to max_length, adding ellipsis if truncated."""
    if len(s) <= max_length:
        return s
    # Ensure ellipsis is included in max_length
    if max_length <= 3:
        return "..."[:max_length]
    return s[:max_length - 3] + "..."
