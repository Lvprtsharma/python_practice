"""
Problem: Longest substring without repeating characters.
Example: Input: 'abcabcbb' Output: 3 ('abc')

Approaches:
1. Sliding window with set
2. Sliding window with dict (optimized)
3. Brute-force (for completeness)
"""

def length_of_longest_substring_set(s):
    """
    Method 1: Sliding window with set
    """
    n = len(s)
    seen = set()
    left = right = 0
    max_len = 0
    while right < n:
        if s[right] not in seen:
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        else:
            seen.remove(s[left])
            left += 1
    return max_len

def length_of_longest_substring_dict(s):
    """
    Method 2: Sliding window with dict (optimized)
    """
    n = len(s)
    char_index = {}
    max_len = start = 0
    for i, c in enumerate(s):
        if c in char_index and char_index[c] >= start:
            start = char_index[c] + 1
        char_index[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len

def length_of_longest_substring_bruteforce(s):
    """
    Method 3: Brute-force (for completeness)
    """
    n = len(s)
    max_len = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len

if __name__ == "__main__":
    test_str = "abcabcbb"
    print(f"Set: {length_of_longest_substring_set(test_str)}")
    print(f"Dict: {length_of_longest_substring_dict(test_str)}")
    print(f"Brute-force: {length_of_longest_substring_bruteforce(test_str)}") 