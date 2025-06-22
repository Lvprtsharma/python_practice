"""
Problem: Flip the words in a sentence, not the letters.
Example: Input: 'hello world' Output: 'world hello'

Approaches:
1. Using split, reverse, join (Pythonic)
2. Manual split and build
3. Using stack
"""

def reverse_words_split(s):
    """
    Method 1: Using split, reverse, join
    """
    return ' '.join(s.split()[::-1])

def reverse_words_manual(s):
    """
    Method 2: Manual split and build
    """
    words = []
    word = ''
    for c in s:
        if c == ' ':
            if word:
                words.append(word)
                word = ''
        else:
            word += c
    if word:
        words.append(word)
    return ' '.join(words[::-1])

def reverse_words_stack(s):
    """
    Method 3: Using stack
    """
    words = s.split()
    stack = []
    for word in words:
        stack.append(word)
    result = []
    while stack:
        result.append(stack.pop())
    return ' '.join(result)

if __name__ == "__main__":
    test_str = "hello world from python"
    print(f"Split: {reverse_words_split(test_str)}")
    print(f"Manual: {reverse_words_manual(test_str)}")
    print(f"Stack: {reverse_words_stack(test_str)}") 