"""
Problem: Remove duplicates from a string efficiently.
Example: Input: 'banana' Output: 'ban'

Approaches:
1. Using set (not order-preserving)
2. Using set with order-preserving loop
3. Using dict.fromkeys (order-preserving, Python 3.7+)
4. Using collections.OrderedDict (for older Python)
"""

def remove_duplicates_set(s):
    """
    Method 1: Using set (not order-preserving)
    """
    return ''.join(set(s))

def remove_duplicates_ordered(s):
    """
    Method 2: Using set with order-preserving loop
    """
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def remove_duplicates_dict(s):
    """
    Method 3: Using dict.fromkeys (order-preserving, Python 3.7+)
    """
    return ''.join(dict.fromkeys(s))

def remove_duplicates_ordereddict(s):
    """
    Method 4: Using collections.OrderedDict (for older Python)
    """
    from collections import OrderedDict
    return ''.join(OrderedDict.fromkeys(s))

if __name__ == "__main__":
    test_str = "banana"
    print(f"Original: {test_str}")
    print(f"Set: {remove_duplicates_set(test_str)}")
    print(f"Ordered: {remove_duplicates_ordered(test_str)}")
    print(f"Dict: {remove_duplicates_dict(test_str)}")
    print(f"OrderedDict: {remove_duplicates_ordereddict(test_str)}") 