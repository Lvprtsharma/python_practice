"""
Problem: Product of all elements except self.
Example: Input: [1,2,3,4] Output: [24,12,8,6]

Approaches:
1. Left and right product arrays (no division)
2. Using division (if allowed)
3. Prefix and suffix products (single pass)
"""

def product_except_self_no_division(nums):
    """
    Method 1: Left and right product arrays (no division)
    """
    n = len(nums)
    left = [1]*n
    right = [1]*n
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    return [left[i]*right[i] for i in range(n)]

def product_except_self_division(nums):
    """
    Method 2: Using division (if allowed, handles zeros)
    """
    n = len(nums)
    zero_count = nums.count(0)
    if zero_count > 1:
        return [0]*n
    total = 1
    for num in nums:
        if num != 0:
            total *= num
    return [0 if num == 0 else total//num for num in nums]

def product_except_self_prefix_suffix(nums):
    """
    Method 3: Prefix and suffix products (single pass, no division)
    """
    n = len(nums)
    res = [1]*n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res

if __name__ == "__main__":
    numbers = [1,2,3,4]
    print(f"No division: {product_except_self_no_division(numbers)}")
    print(f"Division: {product_except_self_division(numbers)}")
    print(f"Prefix/suffix: {product_except_self_prefix_suffix(numbers)}") 