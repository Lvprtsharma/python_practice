"""
Problem: Check if a number is prime.
Example: Input: 7 Output: True

Explanation:
A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
There are several ways to check for prime numbers:
1. Basic trial division up to sqrt(n)
2. Optimized trial division (checking only up to sqrt(n) and skipping even numbers)
3. Sieve of Eratosthenes (for finding all primes up to n)
4. Miller-Rabin primality test (for very large numbers)
5. Fermat primality test (probabilistic test)
"""

def is_prime(n):
    """
    Method 1: Basic trial division
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n):
    """
    Method 2: Optimized trial division
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    Note: Checks 2 separately and then only odd numbers
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check only odd numbers up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    """
    Method 3: Sieve of Eratosthenes
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    Note: Returns all prime numbers up to n
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(n + 1) if sieve[i]]

def miller_rabin_test(n, k=5):
    """
    Method 4: Miller-Rabin primality test
    Time Complexity: O(k log³ n)
    Space Complexity: O(1)
    Note: Probabilistic test, k determines accuracy
    """
    import random
    
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    def miller_test(d, n):
        a = 2 + random.randint(1, n - 4)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            return True
            
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            
            if x == 1:
                return False
            if x == n - 1:
                return True
        
        return False
    
    d = n - 1
    while d % 2 == 0:
        d //= 2
        
    for _ in range(k):
        if not miller_test(d, n):
            return False
    return True

def fermat_primality_test(n, k=5):
    """
    Method 5: Fermat primality test
    Time Complexity: O(k log n)
    Space Complexity: O(1)
    Note: Probabilistic test, may fail for Carmichael numbers
    """
    import random
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    for _ in range(k):
        a = random.randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
    return True

# Example usage
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 7, 11, 15, 17, 20, 23, 29, 97]
    
    print("Testing different prime checking methods:")
    for num in test_numbers:
        print(f"\nNumber: {num}")
        print(f"Method 1 (Basic): {is_prime(num)}")
        print(f"Method 2 (Optimized): {is_prime_optimized(num)}")
        print(f"Method 4 (Miller-Rabin): {miller_rabin_test(num)}")
        print(f"Method 5 (Fermat): {fermat_primality_test(num)}")
    
    # Demonstrate Sieve for finding all primes up to 30
    n = 30
    print(f"\nAll prime numbers up to {n}:")
    print(f"Sieve of Eratosthenes: {sieve_of_eratosthenes(n)}")
    
    # Performance comparison
    import time
    
    large_prime = 104729  # 10000th prime number
    print(f"\nPerformance comparison for n = {large_prime}:")
    
    for method in [is_prime, is_prime_optimized, miller_rabin_test, fermat_primality_test]:
        start = time.time()
        result = method(large_prime)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 