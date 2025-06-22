"""
Problem: Most frequent character in a string.
Example: Input: 'aabbbcc' Output: 'b'

Approaches:
1. Using collections.Counter
2. Using dict and max
3. Using sort and groupby
"""

def most_frequent_counter(s):
    """
    Method 1: Using Counter
    """
    from collections import Counter
    count = Counter(s)
    return count.most_common(1)[0][0] if count else None

def most_frequent_dict(s):
    """
    Method 2: Using dict and max
    """
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return max(freq, key=freq.get) if freq else None

def most_frequent_groupby(s):
    """
    Method 3: Using sort and groupby
    """
    from itertools import groupby
    s_sorted = sorted(s)
    return max(((char, sum(1 for _ in group)) for char, group in groupby(s_sorted)), key=lambda x: x[1])[0] if s else None

if __name__ == "__main__":
    test_str = "aabbbcc"
    print(f"Counter: {most_frequent_counter(test_str)}")
    print(f"Dict: {most_frequent_dict(test_str)}")
    print(f"Groupby: {most_frequent_groupby(test_str)}") 