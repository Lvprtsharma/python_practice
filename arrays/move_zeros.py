"""
Problem: Move all zeros to the end — keep order.
Example: Input: [0, 1, 0, 3, 12] Output: [1, 3, 12, 0, 0]

Approaches:
1. Two-pointer in-place
2. New array and fill
3. Count and fill
"""

def move_zeros_two_pointer(arr):
    """
    Method 1: Two-pointer in-place
    """
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    for i in range(pos, len(arr)):
        arr[i] = 0
    return arr

def move_zeros_new_array(arr):
    """
    Method 2: New array and fill
    """
    result = [x for x in arr if x != 0]
    result += [0] * (len(arr) - len(result))
    return result

def move_zeros_count_fill(arr):
    """
    Method 3: Count and fill
    """
    count = arr.count(0)
    result = [x for x in arr if x != 0]
    result.extend([0] * count)
    return result

if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12]
    print(f"Two-pointer: {move_zeros_two_pointer(numbers[:])}")
    print(f"New array: {move_zeros_new_array(numbers)}")
    print(f"Count/fill: {move_zeros_count_fill(numbers)}") 