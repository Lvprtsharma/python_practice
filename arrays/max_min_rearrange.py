"""
Problem: Rearrange array in max-min order alternately.
Example: Input: [1,2,3,4,5,6] Output: [6,1,5,2,4,3]

Approaches:
1. Two-pointer with new array
2. In-place encoding (for positive integers)
3. List comprehension (for new array)
"""

def max_min_rearrange_two_pointer(arr):
    """
    Method 1: Two-pointer with new array
    """
    n = len(arr)
    result = []
    left, right = 0, n-1
    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])
        left += 1
        right -= 1
    return result

def max_min_rearrange_inplace(arr):
    """
    Method 2: In-place encoding (for positive integers)
    """
    n = len(arr)
    max_idx = n - 1
    min_idx = 0
    max_elem = arr[-1] + 1
    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1
    for i in range(n):
        arr[i] //= max_elem
    return arr

def max_min_rearrange_comprehension(arr):
    """
    Method 3: List comprehension (for new array)
    """
    n = len(arr)
    return [arr[n-1-i//2] if i%2==0 else arr[i//2] for i in range(n)]

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6]
    print(f"Two-pointer: {max_min_rearrange_two_pointer(numbers)}")
    print(f"In-place: {max_min_rearrange_inplace(numbers[:])}")
    print(f"Comprehension: {max_min_rearrange_comprehension(numbers)}") 