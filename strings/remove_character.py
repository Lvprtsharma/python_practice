"""
Problem: Remove a specific character — cleanly.
Example: Input: 'banana', remove 'a' Output: 'bnn'

Approaches:
1. Using str.replace
2. List comprehension
3. Using filter
"""

def remove_char_replace(s, ch):
    """
    Method 1: Using str.replace
    """
    return s.replace(ch, '')

def remove_char_comprehension(s, ch):
    """
    Method 2: List comprehension
    """
    return ''.join([c for c in s if c != ch])

def remove_char_filter(s, ch):
    """
    Method 3: Using filter
    """
    return ''.join(filter(lambda c: c != ch, s))

if __name__ == "__main__":
    test_str = "banana"
    ch = 'a'
    print(f"Replace: {remove_char_replace(test_str, ch)}")
    print(f"Comprehension: {remove_char_comprehension(test_str, ch)}")
    print(f"Filter: {remove_char_filter(test_str, ch)}") 