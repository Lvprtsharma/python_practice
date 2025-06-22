"""
Problem: Is one string a rotation of another?
Example: Input: 'waterbottle', 'erbottlewat' Output: True

Approaches:
1. Concatenation and substring check
2. Queue-based rotation
"""

def is_rotation_concat(s1, s2):
    """
    Method 1: Concatenation and substring check
    """
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

def is_rotation_queue(s1, s2):
    """
    Method 2: Queue-based rotation
    """
    from collections import deque
    if len(s1) != len(s2):
        return False
    dq = deque(s1)
    for _ in range(len(s1)):
        dq.rotate(1)
        if ''.join(dq) == s2:
            return True
    return False

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(f"Concat: {is_rotation_concat(s1, s2)}")
    print(f"Queue: {is_rotation_queue(s1, s2)}") 