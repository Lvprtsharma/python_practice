"""
Problem: Turn full sentences into acronyms.
Example: Input: 'Portable Network Graphics' Output: 'PNG'

Approaches:
1. Using split and upper
2. Using regex
3. List comprehension
"""

def acronym_split(s):
    """
    Method 1: Using split and upper
    """
    return ''.join(word[0].upper() for word in s.split() if word)

def acronym_regex(s):
    """
    Method 2: Using regex
    """
    import re
    return ''.join(re.findall(r'\b\w', s)).upper()

def acronym_comprehension(s):
    """
    Method 3: List comprehension
    """
    return ''.join([c.upper() for i, c in enumerate(s) if (i == 0 or s[i-1] == ' ') and c != ' '])

if __name__ == "__main__":
    test_str = "Portable Network Graphics"
    print(f"Split: {acronym_split(test_str)}")
    print(f"Regex: {acronym_regex(test_str)}")
    print(f"Comprehension: {acronym_comprehension(test_str)}") 