"""
Problem: Find the factorial of a number.
Example: Input: 5 Output: 120
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num}: {factorial(num)}") 