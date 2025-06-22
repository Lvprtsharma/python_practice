"""
Problem: Check for duplicates in an array.
Example: Input: [1, 2, 3, 2] Output: True

Approaches:
1. Using set
2. Sorting and comparing neighbors
3. Using dict
"""

def has_duplicates_set(arr):
    """
    Method 1: Using set
    """
    return len(arr) != len(set(arr))

def has_duplicates_sort(arr):
    """
    Method 2: Sorting and comparing neighbors
    """
    arr_sorted = sorted(arr)
    for i in range(1, len(arr_sorted)):
        if arr_sorted[i] == arr_sorted[i-1]:
            return True
    return False

def has_duplicates_dict(arr):
    """
    Method 3: Using dict
    """
    seen = {}
    for x in arr:
        if x in seen:
            return True
        seen[x] = True
    return False

if __name__ == "__main__":
    numbers = [1, 2, 3, 2]
    print(f"Set: {has_duplicates_set(numbers)}")
    print(f"Sort: {has_duplicates_sort(numbers)}")
    print(f"Dict: {has_duplicates_dict(numbers)}") 