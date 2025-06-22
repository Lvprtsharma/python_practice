"""
Problem: List all possible substrings of a string.
Example: Input: 'abc' Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']

Approaches:
1. Nested loops
2. List comprehension
"""

def all_substrings_loops(s):
    """
    Method 1: Nested loops
    """
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

def all_substrings_comprehension(s):
    """
    Method 2: List comprehension
    """
    n = len(s)
    return [s[i:j] for i in range(n) for j in range(i+1, n+1)]

if __name__ == "__main__":
    test_str = "abc"
    print(f"Loops: {all_substrings_loops(test_str)}")
    print(f"Comprehension: {all_substrings_comprehension(test_str)}") 