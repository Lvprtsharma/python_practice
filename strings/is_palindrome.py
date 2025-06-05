"""
Problem: Check if a given string is a palindrome.
Example: Input: 'racecar' Output: True

Explanation:
A palindrome is a string that reads the same forwards and backwards.
There are multiple approaches to check for palindromes:
1. Compare string with its reverse (Most Pythonic)
2. Two-pointer technique (Most efficient)
3. Recursive approach
4. Using a loop to compare characters
"""

def is_palindrome(s):
    """
    Method 1: Using string reversal (Most Pythonic)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return s == s[::-1]

def is_palindrome_alt1(s):
    """
    Method 2: Two-pointer technique (Most efficient)
    Time Complexity: O(n/2)
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_alt2(s):
    """
    Method 3: Recursive approach
    Time Complexity: O(n/2)
    Space Complexity: O(n/2) due to recursive call stack
    """
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome_alt2(s[1:-1])

def is_palindrome_alt3(s, ignore_case=True, ignore_spaces=True):
    """
    Method 4: Advanced palindrome check with options
    - Ignores case (optional)
    - Ignores spaces (optional)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if ignore_case:
        s = s.lower()
    if ignore_spaces:
        s = ''.join(s.split())
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "hello",
        "Madam Im Adam"
    ]
    
    for test_str in test_cases:
        print(f"\nTesting: '{test_str}'")
        print(f"Method 1 (reverse): {is_palindrome(test_str)}")
        print(f"Method 2 (two-pointer): {is_palindrome_alt1(test_str)}")
        print(f"Method 3 (recursive): {is_palindrome_alt2(test_str)}")
        print(f"Method 4 (advanced - ignore case/space): {is_palindrome_alt3(test_str)}") 