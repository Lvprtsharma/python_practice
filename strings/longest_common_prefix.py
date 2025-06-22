"""
Problem: Find the longest common prefix among words.
Example: Input: ['flower', 'flow', 'flight'] Output: 'fl'

Approaches:
1. Vertical scanning
2. Horizontal scanning
3. Using zip and set
"""

def longest_common_prefix_vertical(strs):
    """
    Method 1: Vertical scanning
    """
    if not strs:
        return ''
    for i in range(len(strs[0])):
        char = strs[0][i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return strs[0][:i]
    return strs[0]

def longest_common_prefix_horizontal(strs):
    """
    Method 2: Horizontal scanning
    """
    if not strs:
        return ''
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix

def longest_common_prefix_zip(strs):
    """
    Method 3: Using zip and set
    """
    if not strs:
        return ''
    prefix = ''
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix

if __name__ == "__main__":
    words = ["flower", "flow", "flight"]
    print(f"Vertical: {longest_common_prefix_vertical(words)}")
    print(f"Horizontal: {longest_common_prefix_horizontal(words)}")
    print(f"Zip: {longest_common_prefix_zip(words)}") 