"""
Problem: Count how many times each character appears in a string.
Example: Input: 'hello' Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

Approaches:
1. Using collections.Counter
2. Using dict with loop
3. Using defaultdict
"""

def char_frequency_counter(s):
    """
    Method 1: Using Counter
    """
    from collections import Counter
    return dict(Counter(s))

def char_frequency_dict(s):
    """
    Method 2: Using dict with loop
    """
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

def char_frequency_defaultdict(s):
    """
    Method 3: Using defaultdict
    """
    from collections import defaultdict
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1
    return dict(freq)

if __name__ == "__main__":
    test_str = "hello"
    print(f"Counter: {char_frequency_counter(test_str)}")
    print(f"Dict: {char_frequency_dict(test_str)}")
    print(f"DefaultDict: {char_frequency_defaultdict(test_str)}") 