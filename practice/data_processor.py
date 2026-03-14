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
    """
    passed = []
    failed = []
    
    for score in scores:
        # 60 and above is passing
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
    """
    valid_emails = []
    
    for email in email_list:
        # Check for empty/whitespace and proper format
        if email and email.strip() and '@' in email and '.' in email:
            valid_emails.append(email)
    
    return valid_emails


def merge_and_sort_lists(list1, list2):
    """
    Merge two lists and return sorted result.
    """
    # Efficiently merge using list concatenation
    result = list1 + list2
    
    # Return sorted copy without modifying originals
    return sorted(result)


def count_word_occurrences(text, word):
    """
    Count how many times a word appears in text.
    """
    count = 0
    words = text.split()
    
    for w in words:
        # Case-insensitive exact match (strip punctuation)
        if w.lower().strip('.,!?;:') == word.lower():
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
