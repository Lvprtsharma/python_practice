"""
Problem: Replace spaces with %20 — classic URL trick.
Example: Input: 'Mr John Smith' Output: 'Mr%20John%20Smith'

Approaches:
1. Using str.replace
2. Manual list building
3. Using regex
"""

def replace_spaces_builtin(s):
    """
    Method 1: Using str.replace
    """
    return s.replace(' ', '%20')

def replace_spaces_manual(s):
    """
    Method 2: Manual list building
    """
    result = []
    for c in s:
        if c == ' ':
            result.append('%20')
        else:
            result.append(c)
    return ''.join(result)

def replace_spaces_regex(s):
    """
    Method 3: Using regex
    """
    import re
    return re.sub(r'\s', '%20', s)

if __name__ == "__main__":
    test_str = "Mr John Smith"
    print(f"Builtin: {replace_spaces_builtin(test_str)}")
    print(f"Manual: {replace_spaces_manual(test_str)}")
    print(f"Regex: {replace_spaces_regex(test_str)}") 