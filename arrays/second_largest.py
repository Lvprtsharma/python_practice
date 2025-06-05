"""
Problem: Find the second largest number in a list.
Example: Input: [1, 3, 4, 5, 0, 2] Output: 4

Explanation:
There are several ways to find the second largest number:
1. Using set and sorted (Most Pythonic)
2. Using two variables to track largest and second largest
3. Using heap (priority queue)
4. Using sorting
5. Using reduce function
"""

def second_largest(lst):
    """
    Method 1: Using set and sorted
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Note: Handles duplicates automatically
    """
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

def second_largest_tracking(lst):
    """
    Method 2: Using two variables
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: Most efficient approach
    """
    if len(lst) < 2:
        return None
    
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None

def second_largest_heap(lst):
    """
    Method 3: Using heap (priority queue)
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Note: Good for streaming data
    """
    import heapq
    if len(lst) < 2:
        return None
    
    # Remove duplicates and convert to negative for max heap
    unique_nums = list(set(-x for x in lst))
    heapq.heapify(unique_nums)
    
    if len(unique_nums) < 2:
        return None
    
    # Pop largest
    heapq.heappop(unique_nums)
    # Return second largest (negative of the smallest negative)
    return -heapq.heappop(unique_nums)

def second_largest_sorting(lst):
    """
    Method 4: Using sorting
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    Note: Simple but not most efficient
    """
    if len(lst) < 2:
        return None
    
    sorted_lst = sorted(set(lst), reverse=True)
    return sorted_lst[1] if len(sorted_lst) >= 2 else None

def second_largest_reduce(lst):
    """
    Method 5: Using reduce
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: Functional programming approach
    """
    from functools import reduce
    
    def update_top_two(top_two, num):
        first, second = top_two
        if num > first:
            return (num, first)
        elif num > second and num != first:
            return (first, num)
        return top_two
    
    if len(lst) < 2:
        return None
    
    unique_nums = set(lst)
    if len(unique_nums) < 2:
        return None
    
    first_num = max(unique_nums)
    unique_nums.remove(first_num)
    second_num = max(unique_nums)
    
    return second_num

def analyze_numbers(lst):
    """
    Bonus: Detailed number analysis
    Returns various statistics about the list
    """
    if not lst:
        return {
            "error": "Empty list"
        }
    
    return {
        "original_list": lst,
        "unique_count": len(set(lst)),
        "max": max(lst),
        "second_max": second_largest(lst),
        "all_sorted": sorted(lst, reverse=True),
        "duplicates": [x for x in set(lst) if lst.count(x) > 1]
    }

# Example usage
if __name__ == "__main__":
    test_cases = [
        [1, 3, 4, 5, 0, 2],       # Normal case
        [1, 1, 1, 1],             # All same numbers
        [1],                      # Single element
        [],                       # Empty list
        [1, 2, 2, 3, 3, 4],      # Duplicates
        [5, 5, 4, 4, 3, 3],      # Descending with duplicates
    ]
    
    for test_list in test_cases:
        print(f"\nTesting list: {test_list}")
        print(f"Method 1 (set and sorted): {second_largest(test_list)}")
        print(f"Method 2 (tracking): {second_largest_tracking(test_list)}")
        print(f"Method 3 (heap): {second_largest_heap(test_list)}")
        print(f"Method 4 (sorting): {second_largest_sorting(test_list)}")
        print(f"Method 5 (reduce): {second_largest_reduce(test_list)}")
        
        # Detailed analysis
        print("\nDetailed analysis:")
        analysis = analyze_numbers(test_list)
        for key, value in analysis.items():
            print(f"{key}: {value}")
    
    # Performance comparison
    import time
    import random
    
    # Generate large list
    size = 100000
    large_list = [random.randint(1, 1000000) for _ in range(size)]
    
    print(f"\nPerformance comparison for list of size {size}:")
    
    for method in [second_largest, second_largest_tracking, 
                  second_largest_heap, second_largest_sorting,
                  second_largest_reduce]:
        start = time.time()
        method(large_list)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 