"""
Problem: Sum all digits in an integer.
Example: Input: 1234 Output: 10

Explanation:
There are several ways to sum the digits of a number:
1. Using string conversion (Most Pythonic)
2. Using modulo and division (Mathematical approach)
3. Using recursion
4. Using reduce function
5. Using while loop
"""

def sum_digits(n):
    """
    Method 1: Using string conversion
    Time Complexity: O(log n) - number of digits
    Space Complexity: O(log n)
    Note: Most readable approach
    """
    return sum(int(digit) for digit in str(abs(n)))

def sum_digits_math(n):
    """
    Method 2: Using modulo and division
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Note: Most efficient approach
    """
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def sum_digits_recursive(n):
    """
    Method 3: Using recursion
    Time Complexity: O(log n)
    Space Complexity: O(log n) - due to recursive call stack
    """
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits_recursive(n // 10)

def sum_digits_reduce(n):
    """
    Method 4: Using reduce function
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    Note: Functional programming approach
    """
    from functools import reduce
    return reduce(lambda x, y: int(x) + int(y), str(abs(n)))

def sum_digits_while(n):
    """
    Method 5: Using while loop with string
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    Note: Traditional approach
    """
    n = abs(n)
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def analyze_digits(n):
    """
    Bonus: Detailed digit analysis
    Returns various statistics about the number's digits
    """
    n = abs(n)
    digits = [int(d) for d in str(n)]
    return {
        "original_number": n,
        "digit_count": len(digits),
        "sum": sum(digits),
        "average": sum(digits) / len(digits),
        "max_digit": max(digits),
        "min_digit": min(digits),
        "even_digits": [d for d in digits if d % 2 == 0],
        "odd_digits": [d for d in digits if d % 2 == 1],
        "digit_frequency": {d: digits.count(d) for d in set(digits)}
    }

# Example usage
if __name__ == "__main__":
    test_cases = [
        1234,           # Basic case
        -5678,          # Negative number
        0,              # Zero
        999999,         # Repeated digits
        12345678901,    # Large number
    ]
    
    for num in test_cases:
        print(f"\nTesting number: {num}")
        print(f"Method 1 (string): {sum_digits(num)}")
        print(f"Method 2 (math): {sum_digits_math(num)}")
        print(f"Method 3 (recursive): {sum_digits_recursive(num)}")
        print(f"Method 4 (reduce): {sum_digits_reduce(num)}")
        print(f"Method 5 (while): {sum_digits_while(num)}")
        
        # Detailed analysis
        print("\nDetailed analysis:")
        analysis = analyze_digits(num)
        for key, value in analysis.items():
            print(f"{key}: {value}")
    
    # Performance comparison
    import time
    
    # Generate large number
    large_num = 123456789012345678901234567890
    
    print(f"\nPerformance comparison for number: {large_num}")
    
    for method in [sum_digits, sum_digits_math, sum_digits_recursive,
                  sum_digits_reduce, sum_digits_while]:
        start = time.time()
        method(large_num)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 