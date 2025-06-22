"""
Problem: Count how many words are in the string.
Example: Input: 'Hello world!' Output: 2

Approaches:
1. Using split
2. Using regex
3. Manual loop
"""

def word_count_split(s):
    """
    Method 1: Using split
    """
    return len(s.split())

def word_count_regex(s):
    """
    Method 2: Using regex
    """
    import re
    return len(re.findall(r'\b\w+\b', s))

def word_count_manual(s):
    """
    Method 3: Manual loop
    """
    in_word = False
    count = 0
    for c in s:
        if c.isalnum():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count

if __name__ == "__main__":
    test_str = "Hello world! This is a test."
    print(f"Split: {word_count_split(test_str)}")
    print(f"Regex: {word_count_regex(test_str)}")
    print(f"Manual: {word_count_manual(test_str)}") 