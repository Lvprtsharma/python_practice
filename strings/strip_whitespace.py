"""
Problem: Strip all white spaces from a string.
Example: Input: ' a b c ' Output: 'abc'

Approaches:
1. Using str.replace
2. Using join and split
3. Using regex
"""

def strip_whitespace_replace(s):
    """
    Method 1: Using str.replace
    """
    return s.replace(' ', '')

def strip_whitespace_join_split(s):
    """
    Method 2: Using join and split
    """
    return ''.join(s.split())

def strip_whitespace_regex(s):
    """
    Method 3: Using regex
    """
    import re
    return re.sub(r'\s+', '', s)

if __name__ == "__main__":
    test_str = " a b c  d\te\nf "
    print(f"Replace: {strip_whitespace_replace(test_str)}")
    print(f"Join/Split: {strip_whitespace_join_split(test_str)}")
    print(f"Regex: {strip_whitespace_regex(test_str)}") 