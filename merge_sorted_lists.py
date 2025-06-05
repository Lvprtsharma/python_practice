"""
Problem: Merge two sorted lists into one sorted list.
Example: Input: [1, 3, 5], [2, 4, 6] Output: [1, 2, 3, 4, 5, 6]

Explanation:
There are several ways to merge sorted lists:
1. Two-pointer technique (Most efficient)
2. Using built-in sorted() function
3. Using heapq.merge
4. Using recursion
5. Using divide and conquer
"""

def merge_sorted_lists(lst1, lst2):
    """
    Method 1: Two-pointer technique
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    Note: Most efficient approach
    """
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

def merge_sorted_lists_simple(lst1, lst2):
    """
    Method 2: Using sorted()
    Time Complexity: O((n+m)log(n+m))
    Space Complexity: O(n + m)
    Note: Simple but less efficient
    """
    return sorted(lst1 + lst2)

def merge_sorted_lists_heap(lst1, lst2):
    """
    Method 3: Using heapq.merge
    Time Complexity: O(n + m)
    Space Complexity: O(1) for iterator, O(n + m) for list conversion
    Note: Memory efficient for large lists
    """
    from heapq import merge
    return list(merge(lst1, lst2))

def merge_sorted_lists_recursive(lst1, lst2):
    """
    Method 4: Using recursion
    Time Complexity: O(n + m)
    Space Complexity: O(n + m) due to recursive call stack
    """
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    
    if lst1[0] <= lst2[0]:
        return [lst1[0]] + merge_sorted_lists_recursive(lst1[1:], lst2)
    return [lst2[0]] + merge_sorted_lists_recursive(lst1, lst2[1:])

def merge_k_sorted_lists(lists):
    """
    Method 5: Merge K sorted lists using divide and conquer
    Time Complexity: O(N log k) where N is total elements and k is number of lists
    Space Complexity: O(N)
    """
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2
    left = merge_k_sorted_lists(lists[:mid])
    right = merge_k_sorted_lists(lists[mid:])
    return merge_sorted_lists(left, right)

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2, 3], [4, 5, 6]),
        ([], [1, 2, 3]),
        ([1], []),
        ([1, 5, 9], [2, 2, 2, 2]),
    ]
    
    for lst1, lst2 in test_cases:
        print(f"\nMerging lists: {lst1} and {lst2}")
        print(f"Method 1 (two-pointer): {merge_sorted_lists(lst1, lst2)}")
        print(f"Method 2 (sorted): {merge_sorted_lists_simple(lst1, lst2)}")
        print(f"Method 3 (heap): {merge_sorted_lists_heap(lst1, lst2)}")
        print(f"Method 4 (recursive): {merge_sorted_lists_recursive(lst1, lst2)}")
    
    # Test merging K sorted lists
    k_lists = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    print(f"\nMerging K sorted lists: {k_lists}")
    print(f"Result: {merge_k_sorted_lists(k_lists)}")
    
    # Performance comparison
    import time
    import random
    
    # Generate large sorted lists
    size = 10000
    lst1 = sorted([random.randint(1, 1000000) for _ in range(size)])
    lst2 = sorted([random.randint(1, 1000000) for _ in range(size)])
    
    print(f"\nPerformance comparison for lists of size {size}:")
    
    for method in [merge_sorted_lists, merge_sorted_lists_simple, 
                  merge_sorted_lists_heap, merge_sorted_lists_recursive]:
        start = time.time()
        method(lst1, lst2)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 