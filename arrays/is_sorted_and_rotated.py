"""
Problem: Check if array is sorted and rotated.
Example: Input: [3,4,5,1,2] Output: True

Approaches:
1. Count breaks in order
2. Find min index and check sortedness
3. Simulate all rotations
"""

def is_sorted_and_rotated_breaks(arr):
    """
    Method 1: Count breaks in order
    """
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            count += 1
    return count == 1

def is_sorted_and_rotated_min_index(arr):
    """
    Method 2: Find min index and check sortedness
    """
    n = len(arr)
    min_idx = arr.index(min(arr))
    for i in range(n-1):
        if arr[(min_idx+i)%n] > arr[(min_idx+i+1)%n]:
            return False
    return True

def is_sorted_and_rotated_simulate(arr):
    """
    Method 3: Simulate all rotations
    """
    n = len(arr)
    for i in range(n):
        rotated = arr[i:] + arr[:i]
        if all(rotated[j] <= rotated[j+1] for j in range(n-1)):
            return True
    return False

if __name__ == "__main__":
    numbers = [3,4,5,1,2]
    print(f"Breaks: {is_sorted_and_rotated_breaks(numbers)}")
    print(f"Min index: {is_sorted_and_rotated_min_index(numbers)}")
    print(f"Simulate: {is_sorted_and_rotated_simulate(numbers)}") 