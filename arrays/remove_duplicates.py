"""
Problem: Remove duplicates from a list.
Example: Input: [1, 2, 2, 3, 4, 4, 5] Output: [1, 2, 3, 4, 5]

Approaches:
1. Using set (not order-preserving)
2. Using set with order-preserving loop
3. Using dict.fromkeys (order-preserving, Python 3.7+)
4. Using list comprehension
"""

def remove_duplicates_set(lst):
    """
    Method 1: Using set (not order-preserving)
    """
    return list(set(lst))

def remove_duplicates_ordered(lst):
    """
    Method 2: Using set with order-preserving loop
    """
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

def remove_duplicates_dict(lst):
    """
    Method 3: Using dict.fromkeys (order-preserving, Python 3.7+)
    """
    return list(dict.fromkeys(lst))

def remove_duplicates_comprehension(lst):
    """
    Method 4: Using list comprehension (order-preserving)
    """
    result = []
    [result.append(x) for x in lst if x not in result]
    return result

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original: {numbers}")
    print(f"Set: {remove_duplicates_set(numbers)}")
    print(f"Ordered: {remove_duplicates_ordered(numbers)}")
    print(f"Dict: {remove_duplicates_dict(numbers)}")
    print(f"Comprehension: {remove_duplicates_comprehension(numbers)}") 