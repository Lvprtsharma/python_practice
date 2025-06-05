"""
Problem: Remove duplicates from a list.
Example: Input: [1, 2, 2, 3, 4, 4, 5] Output: [1, 2, 3, 4, 5]
"""

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original: {numbers}")
    print(f"Without duplicates: {remove_duplicates(numbers)}") 