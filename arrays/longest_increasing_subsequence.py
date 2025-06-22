"""
Problem: Find the longest increasing subsequence.
Example: Input: [10,9,2,5,3,7,101,18] Output: 4 ([2,3,7,101])

Approaches:
1. Dynamic Programming O(n^2)
2. Patience Sorting O(n log n)
3. Recursive (for completeness)
"""

def lis_dp(arr):
    """
    Method 1: Dynamic Programming O(n^2)
    """
    if not arr:
        return 0
    n = len(arr)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

def lis_patience(arr):
    """
    Method 2: Patience Sorting O(n log n)
    """
    import bisect
    piles = []
    for num in arr:
        idx = bisect.bisect_left(piles, num)
        if idx == len(piles):
            piles.append(num)
        else:
            piles[idx] = num
    return len(piles)

def lis_recursive(arr):
    """
    Method 3: Recursive (for completeness)
    """
    def helper(prev, curr):
        if curr == len(arr):
            return 0
        taken = 0
        if prev < 0 or arr[curr] > arr[prev]:
            taken = 1 + helper(curr, curr+1)
        not_taken = helper(prev, curr+1)
        return max(taken, not_taken)
    return helper(-1, 0)

if __name__ == "__main__":
    numbers = [10,9,2,5,3,7,101,18]
    print(f"DP: {lis_dp(numbers)}")
    print(f"Patience: {lis_patience(numbers)}")
    print(f"Recursive: {lis_recursive(numbers)}") 