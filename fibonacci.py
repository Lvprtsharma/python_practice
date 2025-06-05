"""
Problem: Generate the Fibonacci sequence up to n terms.
Example: Input: 5 Output: [0, 1, 1, 2, 3]

Explanation:
The Fibonacci sequence is a series where each number is the sum of the two preceding ones.
There are several ways to generate the sequence:
1. Using iteration with two variables (Most efficient)
2. Using recursion (Classic approach)
3. Using dynamic programming (Memoization)
4. Using generator function (Memory efficient)
5. Using matrix exponentiation (Most efficient for large n)
"""

def fibonacci(n):
    """
    Method 1: Using iteration (Most efficient for small n)
    Time Complexity: O(n)
    Space Complexity: O(n) - for storing the sequence
    """
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def fibonacci_recursive(n):
    """
    Method 2: Using recursion
    Time Complexity: O(2^n)
    Space Complexity: O(n) due to recursive call stack
    Note: This is inefficient for large n
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = fibonacci_recursive(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq

def fibonacci_dp(n):
    """
    Method 3: Using dynamic programming (Memoization)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    memo = {}
    
    def fib(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            return k
        memo[k] = fib(k-1) + fib(k-2)
        return memo[k]
    
    return [fib(i) for i in range(n)]

def fibonacci_generator(n):
    """
    Method 4: Using generator function
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: Most memory efficient as it generates one number at a time
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_matrix(n):
    """
    Method 5: Using matrix exponentiation
    Time Complexity: O(log n)
    Space Complexity: O(n) - for storing the sequence
    Note: Most efficient for large n
    """
    def matrix_multiply(a, b):
        return [[a[0][0]*b[0][0] + a[0][1]*b[1][0],
                a[0][0]*b[0][1] + a[0][1]*b[1][1]],
               [a[1][0]*b[0][0] + a[1][1]*b[1][0],
                a[1][0]*b[0][1] + a[1][1]*b[1][1]]]
    
    def matrix_power(matrix, power):
        if power == 0:
            return [[1, 0], [0, 1]]
        if power == 1:
            return matrix
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return matrix_multiply(half, half)
        return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    if n <= 0:
        return []
    
    result = []
    base_matrix = [[1, 1], [1, 0]]
    for i in range(n):
        matrix = matrix_power(base_matrix, i)
        result.append(matrix[1][0])
    return result

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Generating Fibonacci sequence with {n} terms:")
    print(f"Method 1 (iteration): {fibonacci(n)}")
    print(f"Method 2 (recursion): {fibonacci_recursive(n)}")
    print(f"Method 3 (dynamic programming): {fibonacci_dp(n)}")
    print(f"Method 4 (generator): {list(fibonacci_generator(n))}")
    print(f"Method 5 (matrix): {fibonacci_matrix(n)}")
    
    # Performance comparison for larger n
    import time
    
    n_large = 30
    print(f"\nPerformance comparison for n = {n_large}:")
    
    start = time.time()
    fibonacci(n_large)
    print(f"Iteration: {time.time() - start:.6f} seconds")
    
    start = time.time()
    fibonacci_recursive(n_large)
    print(f"Recursion: {time.time() - start:.6f} seconds")
    
    start = time.time()
    fibonacci_dp(n_large)
    print(f"Dynamic Programming: {time.time() - start:.6f} seconds")
    
    start = time.time()
    list(fibonacci_generator(n_large))
    print(f"Generator: {time.time() - start:.6f} seconds")
    
    start = time.time()
    fibonacci_matrix(n_large)
    print(f"Matrix: {time.time() - start:.6f} seconds") 