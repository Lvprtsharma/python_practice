"""
Problem: Find the intersection of two arrays.
Example: Input: [1,2,2,1], [2,2] Output: [2,2]

Approaches:
1. Using Counter (for duplicates)
2. Using set (unique intersection)
3. Two-pointer (for sorted arrays)
"""

def intersection_counter(arr1, arr2):
    """
    Method 1: Using Counter (for duplicates)
    """
    from collections import Counter
    c1, c2 = Counter(arr1), Counter(arr2)
    result = []
    for num in c1:
        if num in c2:
            result.extend([num] * min(c1[num], c2[num]))
    return result

def intersection_set(arr1, arr2):
    """
    Method 2: Using set (unique intersection)
    """
    return list(set(arr1) & set(arr2))

def intersection_two_pointer(arr1, arr2):
    """
    Method 3: Two-pointer (for sorted arrays)
    """
    arr1, arr2 = sorted(arr1), sorted(arr2)
    i = j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return result

if __name__ == "__main__":
    arr1 = [1,2,2,1]
    arr2 = [2,2]
    print(f"Counter: {intersection_counter(arr1, arr2)}")
    print(f"Set: {intersection_set(arr1, arr2)}")
    print(f"Two-pointer: {intersection_two_pointer(arr1, arr2)}") 