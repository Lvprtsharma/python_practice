"""
Problem: Find leaders in an array (no greater element to the right).
Example: Input: [16,17,4,3,5,2] Output: [17,5,2]

Approaches:
1. Reverse traversal
2. Stack
3. Brute-force
"""

def find_leaders_reverse(arr):
    """
    Method 1: Reverse traversal
    """
    n = len(arr)
    max_from_right = arr[-1]
    leaders = [max_from_right]
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    return leaders[::-1]

def find_leaders_stack(arr):
    """
    Method 2: Stack
    """
    stack = []
    max_from_right = float('-inf')
    for num in reversed(arr):
        if num > max_from_right:
            stack.append(num)
            max_from_right = num
    return stack[::-1]

def find_leaders_bruteforce(arr):
    """
    Method 3: Brute-force
    """
    n = len(arr)
    leaders = []
    for i in range(n):
        if all(arr[i] > arr[j] for j in range(i+1, n)):
            leaders.append(arr[i])
    return leaders

if __name__ == "__main__":
    numbers = [16,17,4,3,5,2]
    print(f"Reverse: {find_leaders_reverse(numbers)}")
    print(f"Stack: {find_leaders_stack(numbers)}")
    print(f"Brute-force: {find_leaders_bruteforce(numbers)}") 