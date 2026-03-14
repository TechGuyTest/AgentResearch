"""
Data Processor - Debugging Practice Exercise

This module processes user data and calculates statistics.
There are several intentional bugs and improvement opportunities.
Find and fix them!

Hint: Look for logic errors, edge cases, and inefficient patterns.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of numbers.
        
    Returns:
        The average of the numbers.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_max_value(data_list):
    """
    Find the maximum value in a list.
    
    Args:
        data_list: A list of comparable values.
        
    Returns:
        The maximum value, or None if the list is empty.
    """
    if not data_list:
        return None
    
    max_val = data_list[0]
    for i in range(1, len(data_list)):
        if data_list[i] > max_val:
            max_val = data_list[i]
    
    return max_val


def process_user_scores(scores):
    """
    Process user scores and categorize them.
    Returns dict with 'passed', 'failed', and 'average'.
    
    Args:
        scores: A list of numeric scores.
        
    Returns:
        A dictionary with 'passed' (scores >= 60), 'failed' (scores < 60),
        and 'average' (mean of all scores).
        
    Raises:
        ValueError: If the scores list is empty.
    """
    passed = []
    failed = []
    
    for score in scores:
        if score >= 60:
            passed.append(score)
        else:
            failed.append(score)
    
    avg = calculate_average(scores)
    
    return {
        'passed': passed,
        'failed': failed,
        'average': avg
    }


def filter_valid_emails(email_list):
    """
    Filter out invalid email addresses from a list.
    
    Args:
        email_list: A list of email address strings.
        
    Returns:
        A list of valid email addresses.
        
    A valid email must:
        - Not be empty or whitespace-only
        - Contain exactly one '@' symbol
        - Have non-whitespace text before and after the '@'
        - Contain at least one '.' after the '@'
    """
    valid_emails = []
    
    for email in email_list:
        # Skip empty or whitespace-only strings
        if not email or not email.strip():
            continue
        
        # Check for '@' and '.' with proper structure
        if '@' in email and '.' in email:
            parts = email.split('@')
            # Must have exactly one '@' with non-whitespace text on both sides
            if len(parts) == 2 and parts[0].strip() and parts[1].strip():
                # Must have '.' in the domain part
                if '.' in parts[1]:
                    valid_emails.append(email)
    
    return valid_emails


def merge_and_sort_lists(list1, list2):
    """
    Merge two lists and return sorted result.
    
    BUG HINT: Check for efficiency and potential issues.
    """
    # BUG HINT: This creates a new list each iteration - inefficient!
    result = []
    for item in list1:
        result = result + [item]
    for item in list2:
        result = result + [item]
    
    # BUG: Sorting modifies in place but we're returning anyway
    result.sort()
    return result


def count_word_occurrences(text, word):
    """
    Count how many times a word appears in text.
    
    Args:
        text: The text to search in.
        word: The word to count (case-insensitive).
        
    Returns:
        The number of exact word occurrences.
        
    Note:
        - Matching is case-insensitive
        - Only exact word matches are counted (no partial matches)
    """
    count = 0
    words = text.split()
    word_lower = word.lower()
    
    for w in words:
        # Remove punctuation and compare exactly (case-insensitive)
        cleaned_word = ''.join(c for c in w if c.isalnum()).lower()
        if cleaned_word == word_lower:
            count += 1
    
    return count


# Example usage for testing
if __name__ == "__main__":
    # Test data
    test_scores = [85, 72, 59, 90, 60, 45, 78]
    test_emails = ["user@example.com", "invalid", "test@domain.org", "", " @bad.com"]
    test_text = "The cat sat on the cat mat with the cat"
    
    print("Testing process_user_scores:")
    result = process_user_scores(test_scores)
    print(f"Passed: {result['passed']}")
    print(f"Failed: {result['failed']}")
    print(f"Average: {result['average']}")
    
    print("\nTesting filter_valid_emails:")
    valid = filter_valid_emails(test_emails)
    print(f"Valid emails: {valid}")
    
    print("\nTesting count_word_occurrences:")
    count = count_word_occurrences(test_text, "cat")
    print(f"'cat' appears {count} times")
