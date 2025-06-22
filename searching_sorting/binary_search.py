def binary_search(arr, target):
    """
    Binary Search Algorithm
    
    Args:
        arr (list): A sorted list of elements
        target: The element to search for
        
    Returns:
        int: Index of the target element if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2
        
        # If target is found at mid, return the index
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Recursive Binary Search Algorithm
    
    Args:
        arr (list): A sorted list of elements
        target: The element to search for
        left (int): Left boundary of the search space
        right (int): Right boundary of the search space
        
    Returns:
        int: Index of the target element if found, -1 if not found
    """
    # Base case: element not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # If target is found at mid, return the index
    if arr[mid] == target:
        return mid
    
    # If target is greater, search in right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    
    # If target is smaller, search in left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Sorted array
        [2, 4, 6, 8, 10, 12, 14],         # Even numbers
        [1, 3, 5, 7, 9, 11, 13],          # Odd numbers
        [1, 1, 1, 1, 1],                  # All same elements
        [1],                              # Single element
        []                                # Empty array
    ]
    
    # Test iterative binary search
    print("Testing Iterative Binary Search:")
    for arr in test_arrays:
        print(f"\nArray: {arr}")
        for target in [1, 5, 10, 15]:
            result = binary_search(arr, target)
            if result != -1:
                print(f"Found {target} at index {result}")
            else:
                print(f"{target} not found in array")
    
    # Test recursive binary search
    print("\nTesting Recursive Binary Search:")
    for arr in test_arrays:
        print(f"\nArray: {arr}")
        for target in [1, 5, 10, 15]:
            result = binary_search_recursive(arr, target, 0, len(arr) - 1)
            if result != -1:
                print(f"Found {target} at index {result}")
            else:
                print(f"{target} not found in array") 