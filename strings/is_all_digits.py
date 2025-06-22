"""
Problem: Check if the string is all digits — no alphabets allowed.
Example: Input: '12345' Output: True

Approaches:
1. Using str.isdigit
2. Using regex
3. Manual loop
"""

def is_all_digits_builtin(s):
    """
    Method 1: Using str.isdigit
    """
    return s.isdigit()

def is_all_digits_regex(s):
    """
    Method 2: Using regex
    """
    import re
    return bool(re.fullmatch(r'\d+', s))

def is_all_digits_manual(s):
    """
    Method 3: Manual loop
    """
    return all('0' <= c <= '9' for c in s) and bool(s)

if __name__ == "__main__":
    test_cases = ["12345", "12a45", "", "000"]
    for s in test_cases:
        print(f"Builtin: {is_all_digits_builtin(s)}")
        print(f"Regex: {is_all_digits_regex(s)}")
        print(f"Manual: {is_all_digits_manual(s)}") 