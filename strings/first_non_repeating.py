"""
Problem: First non-repeating character in a string.
Example: Input: 'swiss' Output: 'w'

Approaches:
1. Using collections.OrderedDict
2. Using collections.Counter
3. Using index and count
"""

def first_non_repeating_ordereddict(s):
    """
    Method 1: Using OrderedDict
    """
    from collections import OrderedDict
    d = OrderedDict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    for k, v in d.items():
        if v == 1:
            return k
    return None

def first_non_repeating_counter(s):
    """
    Method 2: Using Counter
    """
    from collections import Counter
    count = Counter(s)
    for c in s:
        if count[c] == 1:
            return c
    return None

def first_non_repeating_index(s):
    """
    Method 3: Using index and count
    """
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return None

if __name__ == "__main__":
    test_str = "swiss"
    print(f"OrderedDict: {first_non_repeating_ordereddict(test_str)}")
    print(f"Counter: {first_non_repeating_counter(test_str)}")
    print(f"Index: {first_non_repeating_index(test_str)}") 