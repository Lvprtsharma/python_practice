"""
Problem: Break a string into a char array — without confusion.
Example: Input: 'hello' Output: ['h', 'e', 'l', 'l', 'o']

Approaches:
1. Using list()
2. Manual loop
3. List comprehension
"""

def to_char_array_builtin(s):
    """
    Method 1: Using list()
    """
    return list(s)

def to_char_array_loop(s):
    """
    Method 2: Manual loop
    """
    arr = []
    for c in s:
        arr.append(c)
    return arr

def to_char_array_comprehension(s):
    """
    Method 3: List comprehension
    """
    return [c for c in s]

if __name__ == "__main__":
    test_str = "hello"
    print(f"Builtin: {to_char_array_builtin(test_str)}")
    print(f"Loop: {to_char_array_loop(test_str)}")
    print(f"Comprehension: {to_char_array_comprehension(test_str)}") 