"""
Problem: Rotate the array left/right by K positions.
Example: Input: [1,2,3,4,5], K=2, right Output: [4,5,1,2,3]

Approaches:
1. Slicing
2. Reversal algorithm
3. Using collections.deque
"""

def rotate_right_slice(arr, k):
    """
    Method 1: Slicing (right rotation)
    """
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

def rotate_left_slice(arr, k):
    """
    Method 1: Slicing (left rotation)
    """
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

def rotate_right_reversal(arr, k):
    """
    Method 2: Reversal algorithm (right rotation, in-place)
    """
    n = len(arr)
    k = k % n
    arr[:] = arr[::-1]
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    return arr

def rotate_left_reversal(arr, k):
    """
    Method 2: Reversal algorithm (left rotation, in-place)
    """
    n = len(arr)
    k = k % n
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    arr[:] = arr[::-1]
    return arr

def rotate_right_deque(arr, k):
    """
    Method 3: Using collections.deque (right rotation)
    """
    from collections import deque
    d = deque(arr)
    d.rotate(k)
    return list(d)

def rotate_left_deque(arr, k):
    """
    Method 3: Using collections.deque (left rotation)
    """
    from collections import deque
    d = deque(arr)
    d.rotate(-k)
    return list(d)

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    k = 2
    print(f"Right slice: {rotate_right_slice(numbers, k)}")
    print(f"Left slice: {rotate_left_slice(numbers, k)}")
    print(f"Right reversal: {rotate_right_reversal(numbers[:], k)}")
    print(f"Left reversal: {rotate_left_reversal(numbers[:], k)}")
    print(f"Right deque: {rotate_right_deque(numbers, k)}")
    print(f"Left deque: {rotate_left_deque(numbers, k)}") 