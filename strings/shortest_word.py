"""
Problem: Find the shortest word in a sentence.
Example: Input: 'I love Python' Output: 'I'

Approaches:
1. Using split and min
2. Using regex
3. Manual loop
"""

def shortest_word_split(s):
    """
    Method 1: Using split and min
    """
    words = s.split()
    return min(words, key=len) if words else ''

def shortest_word_regex(s):
    """
    Method 2: Using regex
    """
    import re
    words = re.findall(r'\b\w+\b', s)
    return min(words, key=len) if words else ''

def shortest_word_manual(s):
    """
    Method 3: Manual loop
    """
    min_word = ''
    min_len = float('inf')
    word = ''
    for c in s + ' ':
        if c.isalnum():
            word += c
        elif word:
            if len(word) < min_len:
                min_len = len(word)
                min_word = word
            word = ''
    return min_word

if __name__ == "__main__":
    test_str = "I love Python programming!"
    print(f"Split: {shortest_word_split(test_str)}")
    print(f"Regex: {shortest_word_regex(test_str)}")
    print(f"Manual: {shortest_word_manual(test_str)}") 