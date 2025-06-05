"""
Problem: Check if two strings are anagrams.
Example: Input: 'listen', 'silent' Output: True

Explanation:
An anagram is a word or phrase formed by rearranging the letters of another.
There are several ways to check if two strings are anagrams:
1. Using sorted() function (Most Pythonic)
2. Using Counter class (Most efficient)
3. Using character frequency dictionary
4. Using array/list counting
5. Using XOR operation (for ASCII strings)
"""

def is_anagram(s1, s2):
    """
    Method 1: Using sorted()
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Note: Simple but not most efficient
    """
    return sorted(s1) == sorted(s2)

def is_anagram_counter(s1, s2):
    """
    Method 2: Using Counter
    Time Complexity: O(n)
    Space Complexity: O(1) - limited by character set
    Note: Most efficient for general strings
    """
    from collections import Counter
    return Counter(s1) == Counter(s2)

def is_anagram_dict(s1, s2):
    """
    Method 3: Using dictionary
    Time Complexity: O(n)
    Space Complexity: O(1) - limited by character set
    Note: Traditional counting approach
    """
    if len(s1) != len(s2):
        return False
        
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

def is_anagram_array(s1, s2):
    """
    Method 4: Using array counting (for ASCII strings)
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: Efficient for ASCII strings
    """
    if len(s1) != len(s2):
        return False
    
    char_count = [0] * 128  # for ASCII
    
    for char in s1:
        char_count[ord(char)] += 1
    
    for char in s2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False
    
    return True

def is_anagram_xor(s1, s2):
    """
    Method 5: Using XOR operation (for ASCII strings)
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: Only works when strings contain each character even number of times
    """
    if len(s1) != len(s2):
        return False
    
    xor_sum = 0
    for char in s1 + s2:
        xor_sum ^= ord(char)
    
    return xor_sum == 0

def analyze_anagram(s1, s2):
    """
    Bonus: Detailed anagram analysis
    Returns character frequency comparison
    """
    from collections import Counter
    c1, c2 = Counter(s1), Counter(s2)
    
    return {
        'is_anagram': c1 == c2,
        's1_unique_chars': dict(c1 - c2),
        's2_unique_chars': dict(c2 - c1),
        'common_chars': dict(c1 & c2)
    }

# Example usage
if __name__ == "__main__":
    test_cases = [
        ('listen', 'silent'),          # Perfect anagram
        ('hello', 'world'),            # Not anagram
        ('debit card', 'bad credit'),  # Anagram with spaces
        ('', ''),                      # Empty strings
        ('a', 'a'),                    # Single character
        ('aaa', 'aaa'),               # Repeated characters
        ('Python', 'python'),          # Case sensitive
    ]
    
    for s1, s2 in test_cases:
        print(f"\nTesting strings: '{s1}' and '{s2}'")
        print(f"Method 1 (sorted): {is_anagram(s1, s2)}")
        print(f"Method 2 (Counter): {is_anagram_counter(s1, s2)}")
        print(f"Method 3 (dictionary): {is_anagram_dict(s1, s2)}")
        print(f"Method 4 (array): {is_anagram_array(s1, s2)}")
        print(f"Method 5 (XOR): {is_anagram_xor(s1, s2)}")
        
        # Detailed analysis
        print("\nDetailed analysis:")
        analysis = analyze_anagram(s1, s2)
        print(f"Is anagram: {analysis['is_anagram']}")
        print(f"Characters unique to '{s1}': {analysis['s1_unique_chars']}")
        print(f"Characters unique to '{s2}': {analysis['s2_unique_chars']}")
        print(f"Common characters: {analysis['common_chars']}")
    
    # Performance comparison
    import time
    import random
    import string
    
    # Generate large strings
    size = 10000
    chars = string.ascii_letters
    s1 = ''.join(random.choice(chars) for _ in range(size))
    s2 = ''.join(random.choice(chars) for _ in range(size))
    
    print(f"\nPerformance comparison for strings of length {size}:")
    
    for method in [is_anagram, is_anagram_counter, is_anagram_dict,
                  is_anagram_array, is_anagram_xor]:
        start = time.time()
        method(s1, s2)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 