"""
Problem: Calculate frequency of all elements in O(n).
Example: Input: [2,3,2,3,5] Output: {2:2, 3:2, 5:1}

Approaches:
1. Using dict
2. Using collections.Counter
3. In-place for 1 to n arrays (special case)
"""

def frequency_dict(arr):
    """
    Method 1: Using dict
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

def frequency_counter(arr):
    """
    Method 2: Using collections.Counter
    """
    from collections import Counter
    return dict(Counter(arr))

def frequency_inplace(arr):
    """
    Method 3: In-place for 1 to n arrays (special case, modifies array)
    """
    n = len(arr)
    for i in range(n):
        arr[arr[i] % n] += n
    freq = {}
    for i in range(n):
        freq[i] = arr[i] // n
    return freq

if __name__ == "__main__":
    numbers = [2,3,2,3,5]
    print(f"Dict: {frequency_dict(numbers)}")
    print(f"Counter: {frequency_counter(numbers)}")
    # For in-place, use a 1 to n array, e.g. [2,3,3,2,5,1,4]
    print(f"In-place: {frequency_inplace([2,3,3,2,5,1,4])}") 