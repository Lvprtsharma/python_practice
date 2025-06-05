"""
Problem: Find the most frequent element in a list.
Example: Input: [1, 3, 2, 1, 4, 1] Output: 1

Explanation:
There are several ways to find the most frequent element:
1. Using max() with list.count() (Most Pythonic)
2. Using collections.Counter (Most efficient)
3. Using dictionary to count occurrences
4. Using sorted() with key function
5. Using defaultdict with max()
"""

def most_frequent(lst):
    """
    Method 1: Using max() with list.count()
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Note: Simple but not efficient for large lists
    """
    return max(set(lst), key=lst.count)

def most_frequent_counter(lst):
    """
    Method 2: Using collections.Counter
    Time Complexity: O(n)
    Space Complexity: O(n)
    Note: Most efficient approach
    """
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]

def most_frequent_dict(lst):
    """
    Method 3: Using dictionary
    Time Complexity: O(n)
    Space Complexity: O(n)
    Note: Traditional counting approach
    """
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return max(count_dict.items(), key=lambda x: x[1])[0]

def most_frequent_sorted(lst):
    """
    Method 4: Using sorted with groupby
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Note: Returns first element if multiple have same frequency
    """
    from itertools import groupby
    return sorted(lst, key=lst.count, reverse=True)[0]

def most_frequent_defaultdict(lst):
    """
    Method 5: Using defaultdict
    Time Complexity: O(n)
    Space Complexity: O(n)
    Note: Similar to dictionary method but with defaultdict
    """
    from collections import defaultdict
    counts = defaultdict(int)
    for item in lst:
        counts[item] += 1
    return max(counts.items(), key=lambda x: x[1])[0]

def analyze_frequencies(lst):
    """
    Bonus: Detailed frequency analysis
    Returns all elements and their frequencies in descending order
    """
    from collections import Counter
    counter = Counter(lst)
    return counter.most_common()

# Example usage
if __name__ == "__main__":
    test_cases = [
        [1, 3, 2, 1, 4, 1],           # Single most frequent
        [1, 2, 2, 1, 3, 3],           # Multiple elements with same frequency
        [1],                          # Single element
        ["a", "b", "a", "c", "a"],    # Strings
        [True, False, True, True],     # Booleans
    ]
    
    for test_list in test_cases:
        print(f"\nTesting list: {test_list}")
        print(f"Method 1 (max with count): {most_frequent(test_list)}")
        print(f"Method 2 (Counter): {most_frequent_counter(test_list)}")
        print(f"Method 3 (dictionary): {most_frequent_dict(test_list)}")
        print(f"Method 4 (sorted): {most_frequent_sorted(test_list)}")
        print(f"Method 5 (defaultdict): {most_frequent_defaultdict(test_list)}")
        
        # Detailed analysis
        print("\nFrequency analysis:")
        for element, freq in analyze_frequencies(test_list):
            print(f"Element {element}: {freq} times")
    
    # Performance comparison
    import time
    import random
    
    # Generate large list
    size = 100000
    large_list = [random.randint(1, 100) for _ in range(size)]
    
    print(f"\nPerformance comparison for list of size {size}:")
    
    for method in [most_frequent, most_frequent_counter, most_frequent_dict,
                  most_frequent_sorted, most_frequent_defaultdict]:
        start = time.time()
        method(large_list)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 