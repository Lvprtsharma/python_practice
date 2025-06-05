"""
Problem: Find all pairs in a list that sum to a specific value.
Example: Input: [1, 2, 3, 4, 5], target=5 Output: [(1, 4), (2, 3)]

Explanation:
There are several ways to find pairs that sum to a target:
1. Using set for O(n) lookup (Most efficient)
2. Using two pointers with sorted array
3. Using nested loops (Brute force)
4. Using binary search
5. Using dictionary/hash map
"""

def pair_sum(lst, target):
    """
    Method 1: Using set
    Time Complexity: O(n)
    Space Complexity: O(n)
    Note: Most efficient approach
    """
    seen = set()
    pairs = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

def pair_sum_two_pointers(lst, target):
    """
    Method 2: Using two pointers
    Time Complexity: O(n log n)
    Space Complexity: O(1) excluding output
    Note: Good when array is already sorted
    """
    lst = sorted(lst)
    left, right = 0, len(lst) - 1
    pairs = set()
    
    while left < right:
        current_sum = lst[left] + lst[right]
        if current_sum == target:
            pairs.add((lst[left], lst[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return list(pairs)

def pair_sum_brute_force(lst, target):
    """
    Method 3: Using nested loops (Brute force)
    Time Complexity: O(n²)
    Space Complexity: O(1) excluding output
    Note: Simple but inefficient for large lists
    """
    pairs = set()
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                pairs.add(tuple(sorted((lst[i], lst[j]))))
    return list(pairs)

def pair_sum_binary_search(lst, target):
    """
    Method 4: Using binary search
    Time Complexity: O(n log n)
    Space Complexity: O(1) excluding output
    Note: Good when array is sorted
    """
    def binary_search(arr, left, right, x):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    lst = sorted(lst)
    pairs = set()
    n = len(lst)
    
    for i in range(n):
        complement = target - lst[i]
        # Search in remaining array
        if binary_search(lst, i + 1, n - 1, complement):
            pairs.add(tuple(sorted((lst[i], complement))))
    
    return list(pairs)

def pair_sum_dict(lst, target):
    """
    Method 5: Using dictionary
    Time Complexity: O(n)
    Space Complexity: O(n)
    Note: Similar to set approach but with frequency counting
    """
    num_dict = {}
    pairs = set()
    
    for num in lst:
        complement = target - num
        if complement in num_dict:
            pairs.add(tuple(sorted((num, complement))))
        num_dict[num] = num_dict.get(num, 0) + 1
    
    return list(pairs)

def analyze_pairs(lst, target):
    """
    Bonus: Detailed pair analysis
    Returns various statistics about the pairs and numbers
    """
    pairs = pair_sum(lst, target)
    return {
        "original_list": lst,
        "target_sum": target,
        "number_of_pairs": len(pairs),
        "pairs": pairs,
        "numbers_used": sorted(set(num for pair in pairs for num in pair)),
        "unused_numbers": sorted(set(lst) - set(num for pair in pairs for num in pair))
    }

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 5),          # Basic case
        ([1, 1, 2, 2, 3, 3], 4),       # Duplicates
        ([1, 2, 3, 4, 5], 10),         # No pairs
        ([-1, 0, 1, 2, 3], 2),         # Negative numbers
        ([0, 0, 0, 0], 0),             # All zeros
    ]
    
    for lst, target in test_cases:
        print(f"\nTesting list: {lst} with target: {target}")
        print(f"Method 1 (set): {pair_sum(lst, target)}")
        print(f"Method 2 (two pointers): {pair_sum_two_pointers(lst, target)}")
        print(f"Method 3 (brute force): {pair_sum_brute_force(lst, target)}")
        print(f"Method 4 (binary search): {pair_sum_binary_search(lst, target)}")
        print(f"Method 5 (dictionary): {pair_sum_dict(lst, target)}")
        
        # Detailed analysis
        print("\nDetailed analysis:")
        analysis = analyze_pairs(lst, target)
        for key, value in analysis.items():
            print(f"{key}: {value}")
    
    # Performance comparison
    import time
    import random
    
    # Generate large list
    size = 10000
    large_list = [random.randint(-1000, 1000) for _ in range(size)]
    target = 500
    
    print(f"\nPerformance comparison for list of size {size}:")
    
    for method in [pair_sum, pair_sum_two_pointers, pair_sum_brute_force,
                  pair_sum_binary_search, pair_sum_dict]:
        start = time.time()
        method(large_list, target)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 