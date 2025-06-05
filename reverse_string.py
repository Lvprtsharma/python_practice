"""
Problem: Reverse a given string.
Example: Input: 'hello' Output: 'olleh'

Explanation:
There are several ways to reverse a string in Python:
1. Using string slicing with step -1 ([::-1]) - Most Pythonic and efficient
2. Using reversed() function and joining characters
3. Using a loop to build the string backwards
4. Using recursion
"""

def reverse_string(s):
    """
    Method 1: Using string slicing (Most Pythonic)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return s[::-1]

def reverse_string_alt1(s):
    """
    Method 2: Using reversed() and join
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return ''.join(reversed(s))

def reverse_string_alt2(s):
    """
    Method 3: Using loop (Traditional way)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_alt3(s):
    """
    Method 4: Using recursion
    Time Complexity: O(n)
    Space Complexity: O(n) - due to recursive call stack
    """
    if len(s) <= 1:
        return s
    return reverse_string_alt3(s[1:]) + s[0]

# Example usage
if __name__ == "__main__":
    test_str = "hello"
    print(f"Original string: {test_str}")
    print(f"Method 1 (slice): {reverse_string(test_str)}")
    print(f"Method 2 (reversed): {reverse_string_alt1(test_str)}")
    print(f"Method 3 (loop): {reverse_string_alt2(test_str)}")
    print(f"Method 4 (recursion): {reverse_string_alt3(test_str)}") 