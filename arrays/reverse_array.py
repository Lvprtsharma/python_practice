"""
Problem: Reverse an array in-place.
Example: Input: [1, 2, 3, 4] Output: [4, 3, 2, 1]

Approaches:
1. Two-pointer swap (in-place)
2. Slicing (creates new array)
3. Built-in reverse()
"""

def reverse_array_two_pointer(arr):
    """
    Method 1: Two-pointer swap (in-place)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def reverse_array_slice(arr):
    """
    Method 2: Slicing (creates new array)
    """
    return arr[::-1]

def reverse_array_builtin(arr):
    """
    Method 3: Built-in reverse()
    """
    arr.reverse()
    return arr

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print(f"Two-pointer: {reverse_array_two_pointer(numbers[:])}")
    print(f"Slice: {reverse_array_slice(numbers)}")
    print(f"Builtin: {reverse_array_builtin(numbers[:])}") 