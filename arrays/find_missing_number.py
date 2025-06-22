"""
Problem: Find the missing number from 1 to N.
Example: Input: [1, 2, 4, 5] Output: 3

Approaches:
1. Sum formula
2. Set difference
3. XOR
"""

def find_missing_sum(arr):
    """
    Method 1: Sum formula
    """
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)

def find_missing_set(arr):
    """
    Method 2: Set difference
    """
    n = len(arr) + 1
    return list(set(range(1, n+1)) - set(arr))[0]

def find_missing_xor(arr):
    """
    Method 3: XOR
    """
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0
    for i in range(1, n+1):
        xor_all ^= i
    for num in arr:
        xor_arr ^= num
    return xor_all ^ xor_arr

if __name__ == "__main__":
    numbers = [1, 2, 4, 5]
    print(f"Sum: {find_missing_sum(numbers)}")
    print(f"Set: {find_missing_set(numbers)}")
    print(f"XOR: {find_missing_xor(numbers)}") 