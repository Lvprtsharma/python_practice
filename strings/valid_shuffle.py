"""
Problem: Is this a valid shuffle of two strings?
Example: Input: 'abc', 'def', 'dabecf' Output: True

Approaches:
1. Sorting and comparison
2. Counter and comparison
3. Two-pointer interleaving
"""

def is_valid_shuffle_sort(s1, s2, s3):
    """
    Method 1: Sorting and comparison
    """
    return sorted(s1 + s2) == sorted(s3)

def is_valid_shuffle_counter(s1, s2, s3):
    """
    Method 2: Counter and comparison
    """
    from collections import Counter
    return Counter(s1 + s2) == Counter(s3)

def is_valid_shuffle_two_pointer(s1, s2, s3):
    """
    Method 3: Two-pointer interleaving
    """
    i = j = k = 0
    while k < len(s3):
        if i < len(s1) and s1[i] == s3[k]:
            i += 1
        elif j < len(s2) and s2[j] == s3[k]:
            j += 1
        else:
            return False
        k += 1
    return i == len(s1) and j == len(s2)

if __name__ == "__main__":
    s1, s2, s3 = "abc", "def", "dabecf"
    print(f"Sort: {is_valid_shuffle_sort(s1, s2, s3)}")
    print(f"Counter: {is_valid_shuffle_counter(s1, s2, s3)}")
    print(f"Two-pointer: {is_valid_shuffle_two_pointer(s1, s2, s3)}") 