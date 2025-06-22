"""
Problem: Implement atoi (string to integer conversion).
Example: Input: '  -42' Output: -42

Approaches:
1. Manual parsing (ignoring built-ins)
2. Handling whitespace and sign
3. Using try/except for completeness
"""

def my_atoi_manual(s):
    """
    Method 1: Manual parsing (ignoring built-ins)
    """
    s = s.strip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + (ord(s[i]) - ord('0'))
        i += 1
    return sign * num

def my_atoi_try(s):
    """
    Method 2: Using try/except (for completeness)
    """
    try:
        return int(s)
    except ValueError:
        return 0

def my_atoi_with_limits(s):
    """
    Method 3: Manual parsing with 32-bit int limits (like LeetCode)
    """
    s = s.strip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1
    num = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    while i < len(s) and s[i].isdigit():
        num = num * 10 + (ord(s[i]) - ord('0'))
        i += 1
    num *= sign
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

if __name__ == "__main__":
    test_cases = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
    for s in test_cases:
        print(f"Manual: {my_atoi_manual(s)}")
        print(f"Try: {my_atoi_try(s)}")
        print(f"With limits: {my_atoi_with_limits(s)}") 