"""
Problem: Find the maximum number in a list.
Example: Input: [1, 5, 2, 9, 3] Output: 9

Explanation:
There are several ways to find the maximum number in a list:
1. Using built-in max() function (Most Pythonic)
2. Using loop to compare elements (Traditional way)
3. Using reduce() function
4. Using sorting
5. Using recursion
"""

def find_max(lst):
    """
    Method 1: Using built-in max() function (Most Pythonic)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    return max(lst)

def find_max_alt1(lst):
    """
    Method 2: Using loop (Traditional way)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not lst:
        return None
    max_num = lst[0]
    for num in lst[1:]:
        if num > max_num:
            max_num = num
    return max_num

def find_max_alt2(lst):
    """
    Method 3: Using reduce() function
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    from functools import reduce
    return reduce(lambda x, y: x if x > y else y, lst) if lst else None

def find_max_alt3(lst):
    """
    Method 4: Using sorting
    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sorting implementation
    """
    return sorted(lst)[-1] if lst else None

def find_max_alt4(lst):
    """
    Method 5: Using recursion
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursive call stack
    """
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    left_max = find_max_alt4(lst[:mid])
    right_max = find_max_alt4(lst[mid:])
    return left_max if left_max > right_max else right_max

# Example usage
if __name__ == "__main__":
    numbers = [1, 5, 2, 9, 3]
    print(f"List: {numbers}")
    print(f"Method 1 (max function): {find_max(numbers)}")
    print(f"Method 2 (loop): {find_max_alt1(numbers)}")
    print(f"Method 3 (reduce): {find_max_alt2(numbers)}")
    print(f"Method 4 (sorting): {find_max_alt3(numbers)}")
    print(f"Method 5 (recursion): {find_max_alt4(numbers)}")

    # Edge cases
    empty_list = []
    single_element = [42]
    negative_numbers = [-5, -2, -8, -1]
    print(f"\nEdge Cases:")
    print(f"Empty list: {find_max_alt1(empty_list)}")
    print(f"Single element: {find_max_alt1(single_element)}")
    print(f"Negative numbers: {find_max_alt1(negative_numbers)}") 