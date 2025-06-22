"""
Problem: Find subarrays with a given sum.
Example: Input: [1,2,3,4,5], sum=5 Output: [[2,3],[5]]

Approaches:
1. Brute-force
2. Hashmap (for positive/negative numbers)
3. Sliding window (for positives only)
"""

def subarrays_with_sum_bruteforce(arr, target):
    """
    Method 1: Brute-force
    """
    n = len(arr)
    result = []
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == target:
                result.append(arr[i:j+1])
    return result

def subarrays_with_sum_hashmap(arr, target):
    """
    Method 2: Hashmap (handles negatives)
    """
    from collections import defaultdict
    curr_sum = 0
    sum_map = defaultdict(list)
    sum_map[0].append(-1)
    result = []
    for i, num in enumerate(arr):
        curr_sum += num
        if (curr_sum - target) in sum_map:
            for start in sum_map[curr_sum - target]:
                result.append(arr[start+1:i+1])
        sum_map[curr_sum].append(i)
    return result

def subarrays_with_sum_sliding_window(arr, target):
    """
    Method 3: Sliding window (positives only)
    """
    n = len(arr)
    result = []
    left = 0
    curr_sum = 0
    for right in range(n):
        curr_sum += arr[right]
        while curr_sum > target and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == target:
            result.append(arr[left:right+1])
    return result

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    target = 5
    print(f"Brute-force: {subarrays_with_sum_bruteforce(numbers, target)}")
    print(f"Hashmap: {subarrays_with_sum_hashmap(numbers, target)}")
    print(f"Sliding window: {subarrays_with_sum_sliding_window(numbers, target)}") 