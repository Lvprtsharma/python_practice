"""
Problem: Find the longest common subsequence between two strings.
Example: Input: str1 = 'ABCDGH', str2 = 'AEDFHR' Output: 'ADH' (length = 3)

Explanation:
The longest common subsequence (LCS) is a classic dynamic programming problem.
There are several ways to implement it:
1. Dynamic Programming with tabulation (Most efficient)
2. Recursive approach
3. Memoization (Top-down DP)
4. Space-optimized DP
5. Using itertools for subsequences
"""

def lcs_dp(str1, str2):
    """
    Method 1: Dynamic Programming with tabulation
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    Note: Most efficient approach
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

def lcs_recursive(str1, str2):
    """
    Method 2: Recursive approach
    Time Complexity: O(2^(m+n))
    Space Complexity: O(m+n) due to recursive call stack
    Note: Inefficient for large strings
    """
    def lcs_helper(str1, str2, m, n):
        if m == 0 or n == 0:
            return ""
        
        if str1[m-1] == str2[n-1]:
            return lcs_helper(str1, str2, m-1, n-1) + str1[m-1]
        else:
            left = lcs_helper(str1, str2, m-1, n)
            right = lcs_helper(str1, str2, m, n-1)
            return left if len(left) > len(right) else right
    
    return lcs_helper(str1, str2, len(str1), len(str2))

def lcs_memoization(str1, str2):
    """
    Method 3: Memoization (Top-down DP)
    Time Complexity: O(mn)
    Space Complexity: O(mn)
    Note: Good for sparse problems
    """
    def lcs_helper(str1, str2, m, n, memo):
        if m == 0 or n == 0:
            return ""
        
        if (m, n) in memo:
            return memo[(m, n)]
        
        if str1[m-1] == str2[n-1]:
            memo[(m, n)] = lcs_helper(str1, str2, m-1, n-1, memo) + str1[m-1]
        else:
            left = lcs_helper(str1, str2, m-1, n, memo)
            right = lcs_helper(str1, str2, m, n-1, memo)
            memo[(m, n)] = left if len(left) > len(right) else right
        
        return memo[(m, n)]
    
    return lcs_helper(str1, str2, len(str1), len(str2), {})

def lcs_space_optimized(str1, str2):
    """
    Method 4: Space-optimized DP
    Time Complexity: O(mn)
    Space Complexity: O(min(m,n))
    Note: Best for memory-constrained environments
    """
    m, n = len(str1), len(str2)
    
    # Make sure str1 is shorter for space optimization
    if m > n:
        str1, str2 = str2, str1
        m, n = n, m
    
    current = [""] * (m + 1)
    previous = [""] * (m + 1)
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[i-1] == str2[j-1]:
                current[i] = previous[i-1] + str1[i-1]
            else:
                current[i] = max(current[i-1], previous[i], key=len)
        current, previous = previous, current
    
    return previous[m]

def lcs_itertools(str1, str2):
    """
    Method 5: Using itertools for subsequences
    Time Complexity: O(2^m * 2^n)
    Space Complexity: O(2^m + 2^n)
    Note: Brute force approach, only suitable for very small strings
    """
    from itertools import combinations
    
    def get_subsequences(s):
        subsequences = set()
        for length in range(1, len(s) + 1):
            for combo in combinations(range(len(s)), length):
                subsequences.add(''.join(s[i] for i in combo))
        return subsequences
    
    # Get all subsequences of both strings
    subsequences1 = get_subsequences(str1)
    subsequences2 = get_subsequences(str2)
    
    # Find common subsequences
    common = subsequences1.intersection(subsequences2)
    
    # Return the longest one
    return max(common, key=len, default="")

def analyze_lcs(str1, str2):
    """
    Bonus: Detailed LCS analysis
    Returns various information about the LCS
    """
    lcs = lcs_dp(str1, str2)
    return {
        "string1": str1,
        "string2": str2,
        "lcs": lcs,
        "lcs_length": len(lcs),
        "string1_length": len(str1),
        "string2_length": len(str2),
        "lcs_positions_in_str1": [i for i, c in enumerate(str1) if c in lcs],
        "lcs_positions_in_str2": [i for i, c in enumerate(str2) if c in lcs],
        "common_chars": sorted(set(str1) & set(str2))
    }

# Example usage
if __name__ == "__main__":
    test_cases = [
        ("ABCDGH", "AEDFHR"),          # Regular case
        ("AGGTAB", "GXTXAYB"),         # Multiple common subsequences
        ("HELLO", "WORLD"),            # Few common characters
        ("ABCDE", "ABCDE"),           # Identical strings
        ("", "ABC"),                   # Empty string
        ("XYZ", "ABC")                 # No common characters
    ]
    
    for str1, str2 in test_cases:
        print(f"\nTesting strings: '{str1}' and '{str2}'")
        print(f"Method 1 (DP): {lcs_dp(str1, str2)}")
        print(f"Method 2 (recursive): {lcs_recursive(str1, str2)}")
        print(f"Method 3 (memoization): {lcs_memoization(str1, str2)}")
        print(f"Method 4 (space optimized): {lcs_space_optimized(str1, str2)}")
        if len(str1) <= 10 and len(str2) <= 10:  # Only for small strings
            print(f"Method 5 (itertools): {lcs_itertools(str1, str2)}")
        
        # Detailed analysis
        print("\nDetailed analysis:")
        analysis = analyze_lcs(str1, str2)
        for key, value in analysis.items():
            print(f"{key}: {value}")
    
    # Performance comparison
    import time
    import random
    import string
    
    # Generate large strings
    size = 100
    str1 = ''.join(random.choices(string.ascii_uppercase, k=size))
    str2 = ''.join(random.choices(string.ascii_uppercase, k=size))
    
    print(f"\nPerformance comparison for strings of length {size}:")
    
    for method in [lcs_dp, lcs_memoization, lcs_space_optimized]:
        start = time.time()
        method(str1, str2)
        print(f"{method.__name__}: {time.time() - start:.6f} seconds") 