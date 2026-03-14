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
    
    BUG HINT: What happens with empty lists?
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_max_value(data_list):
    """
    Find the maximum value in a list.
    
    BUG HINT: Check the comparison logic carefully.
    """
    if not data_list:
        return None
    
    max_val = data_list[0]
    for i in range(1, len(data_list)):
        # BUG: Wrong comparison operator
        if data_list[i] < max_val:
            max_val = data_list[i]
    
    return max_val


def process_user_scores(scores):
    """
    Process user scores and categorize them.
    Returns dict with 'passed', 'failed', and 'average'.
    
    BUG HINT: Check the boundary conditions for pass/fail.
    """
    passed = []
    failed = []
    
    for score in scores:
        # BUG: Should 60 be passing or failing?
        if score > 60:
            passed.append(score)
        else:
            failed.append(score)
    
    # BUG HINT: What if scores is empty?
    avg = calculate_average(scores)
    
    return {
        'passed': passed,
        'failed': failed,
        'average': avg
    }


def filter_valid_emails(email_list):
    """
    Filter out invalid email addresses from a list.
    
    BUG HINT: Check the validation logic and edge cases.
    """
    valid_emails = []
    
    for email in email_list:
        # BUG: This check is incomplete and has issues
        if '@' in email and '.' in email:
            # BUG HINT: What about empty strings or whitespace?
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
    
    BUG HINT: Check case sensitivity and partial matches.
    """
    count = 0
    words = text.split(' ')
    
    for w in words:
        # BUG HINT: Is this comparison correct?
        if word in w:
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
