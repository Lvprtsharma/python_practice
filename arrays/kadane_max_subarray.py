"""
Problem: Kadane's Algorithm — maximum subarray sum.
Example: Input: [-2,1,-3,4,-1,2,1,-5,4] Output: 6 ([4,-1,2,1])

Approaches:
1. Kadane's Algorithm
2. Brute-force
3. Prefix sum
"""

def max_subarray_kadane(arr):
    """
    Method 1: Kadane's Algorithm
    """
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def max_subarray_bruteforce(arr):
    """
    Method 2: Brute-force
    """
    n = len(arr)
    max_sum = arr[0]
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

def max_subarray_prefix_sum(arr):
    """
    Method 3: Prefix sum
    """
    n = len(arr)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    max_sum = arr[0]
    for i in range(n):
        for j in range(i+1, n+1):
            max_sum = max(max_sum, prefix[j] - prefix[i])
    return max_sum

if __name__ == "__main__":
    numbers = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"Kadane: {max_subarray_kadane(numbers)}")
    print(f"Brute-force: {max_subarray_bruteforce(numbers)}")
    print(f"Prefix sum: {max_subarray_prefix_sum(numbers)}") 