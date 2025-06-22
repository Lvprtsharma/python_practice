"""
Problem: Longest palindromic substring — two-pointer style.
Example: Input: 'babad' Output: 'bab' or 'aba'

Approaches:
1. Expand around center (two-pointer)
2. Dynamic programming
3. Brute-force
"""

def longest_palindrome_expand(s):
    """
    Method 1: Expand around center (two-pointer)
    """
    if not s:
        return ''
    start = end = 0
    for i in range(len(s)):
        l1, r1 = expand_from_center(s, i, i)
        l2, r2 = expand_from_center(s, i, i+1)
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end+1]

def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left+1, right-1

def longest_palindrome_dp(s):
    """
    Method 2: Dynamic programming
    """
    n = len(s)
    if n == 0:
        return ''
    dp = [[False]*n for _ in range(n)]
    start = 0
    max_len = 1
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_len = length
    return s[start:start+max_len]

def longest_palindrome_bruteforce(s):
    """
    Method 3: Brute-force
    """
    n = len(s)
    max_len = 0
    res = ''
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > max_len:
                max_len = len(substr)
                res = substr
    return res

if __name__ == "__main__":
    test_str = "babad"
    print(f"Expand: {longest_palindrome_expand(test_str)}")
    print(f"DP: {longest_palindrome_dp(test_str)}")
    print(f"Brute-force: {longest_palindrome_bruteforce(test_str)}") 