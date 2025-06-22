"""
Problem: Compress strings with run-length encoding.
Example: Input: 'aaabbc' Output: 'a3b2c1'

Approaches:
1. Iterative approach
2. Using itertools.groupby
"""

def run_length_encode_iterative(s):
    """
    Method 1: Iterative approach
    """
    if not s:
        return ''
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)

def run_length_encode_groupby(s):
    """
    Method 2: Using itertools.groupby
    """
    from itertools import groupby
    return ''.join(f"{char}{sum(1 for _ in group)}" for char, group in groupby(s))

if __name__ == "__main__":
    test_str = "aaabbc"
    print(f"Iterative: {run_length_encode_iterative(test_str)}")
    print(f"Groupby: {run_length_encode_groupby(test_str)}") 