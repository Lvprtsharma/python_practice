"""
Problem: Count the number of vowels in a string.
Example: Input: 'hello' Output: 2

Explanation:
There are several ways to count vowels in a string:
1. Using sum() with generator expression (Most Pythonic)
2. Using regular expressions
3. Using traditional loop
4. Using collections.Counter
5. Using filter() function
"""

def count_vowels(s):
    """
    Method 1: Using sum with generator expression
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def count_vowels_regex(s):
    """
    Method 2: Using regular expressions
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: More flexible for complex patterns
    """
    import re
    return len(re.findall('[aeiouAEIOU]', s))

def count_vowels_loop(s):
    """
    Method 3: Using traditional loop
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    vowels = set('aeiouAEIOU')
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_vowels_counter(s):
    """
    Method 4: Using collections.Counter
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: Useful when you need to count individual vowels
    """
    from collections import Counter
    vowels = set('aeiouAEIOU')
    counter = Counter(s)
    return sum(counter[char] for char in vowels)

def count_vowels_filter(s):
    """
    Method 5: Using filter function
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    vowels = set('aeiouAEIOU')
    return len(list(filter(lambda x: x in vowels, s)))

def analyze_vowels(s):
    """
    Bonus: Detailed vowel analysis
    Returns count of each vowel and their positions
    """
    vowels = 'aeiouAEIOU'
    analysis = {v: {'count': 0, 'positions': []} for v in vowels}
    
    for i, char in enumerate(s):
        if char in vowels:
            analysis[char]['count'] += 1
            analysis[char]['positions'].append(i)
    
    return {v: data for v, data in analysis.items() if data['count'] > 0}

# Example usage
if __name__ == "__main__":
    test_strings = [
        "hello",
        "HELLO",
        "Hello World",
        "rhythm",  # no vowels
        "AeIoU"   # all vowels
    ]
    
    for test_str in test_strings:
        print(f"\nTesting string: '{test_str}'")
        print(f"Method 1 (sum): {count_vowels(test_str)}")
        print(f"Method 2 (regex): {count_vowels_regex(test_str)}")
        print(f"Method 3 (loop): {count_vowels_loop(test_str)}")
        print(f"Method 4 (counter): {count_vowels_counter(test_str)}")
        print(f"Method 5 (filter): {count_vowels_filter(test_str)}")
        
        # Detailed analysis
        print("\nDetailed vowel analysis:")
        analysis = analyze_vowels(test_str)
        for vowel, data in analysis.items():
            print(f"Vowel '{vowel}': {data['count']} occurrences at positions {data['positions']}")
    
    # Performance comparison
    import time
    
    long_string = "hello" * 100000
    print(f"\nPerformance comparison for string length {len(long_string)}:")
    
    for method in [count_vowels, count_vowels_regex, count_vowels_loop, 
                  count_vowels_counter, count_vowels_filter]:
        start = time.time()
        method(long_string)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 