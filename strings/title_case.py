"""
Problem: Convert text to Title Case — properly.
Example: Input: 'hello world' Output: 'Hello World'

Approaches:
1. Using str.title (for reference)
2. Manual split and capitalize
3. Using regex
"""

def to_title_case_builtin(s):
    """
    Method 1: Using str.title (for reference)
    """
    return s.title()

def to_title_case_manual(s):
    """
    Method 2: Manual split and capitalize
    """
    return ' '.join(word.capitalize() for word in s.split())

def to_title_case_regex(s):
    """
    Method 3: Using regex
    """
    import re
    return re.sub(r'(\b\w)', lambda m: m.group().upper(), s)

if __name__ == "__main__":
    test_str = "hello world from python"
    print(f"Builtin: {to_title_case_builtin(test_str)}")
    print(f"Manual: {to_title_case_manual(test_str)}")
    print(f"Regex: {to_title_case_regex(test_str)}") 