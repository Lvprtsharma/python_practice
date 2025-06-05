# Python Interview Practice Questions

This repository contains a collection of commonly asked Python interview questions with multiple solution approaches, detailed explanations, and performance comparisons.

## Repository Structure

```
python-interview-practice/
├── arrays/                    # Array and list operations
│   ├── find_max.py           # Finding maximum element
│   ├── second_largest.py     # Finding second largest element
│   ├── remove_duplicates.py  # Removing duplicate elements
│   ├── merge_sorted_lists.py # Merging sorted lists
│   ├── most_frequent.py      # Finding most frequent element
│   └── pair_sum.py          # Finding pairs with target sum
│
├── strings/                  # String manipulation problems
│   ├── reverse_string.py    # String reversal
│   ├── is_palindrome.py     # Palindrome checking
│   ├── is_anagram.py        # Anagram checking
│   └── count_vowels.py      # Counting vowels
│
├── math/                    # Mathematical problems
│   ├── factorial.py        # Factorial calculation
│   ├── fibonacci.py        # Fibonacci sequence
│   ├── is_prime.py        # Prime number checking
│   └── sum_digits.py      # Sum of digits
│
├── dynamic_programming/    # Dynamic programming problems
│   └── longest_common_subsequence.py  # LCS problem
│
├── searching_sorting/     # Searching and sorting algorithms
│   └── binary_search.py  # Binary search implementations
│
└── oop/                  # Object-oriented programming
    └── person_class.py   # Person class implementation
```

## Questions Overview

### Arrays and Lists (`arrays/`)
1. [Find Maximum](arrays/find_max.py)
   - Using built-in max()
   - Loop-based approach
   - Reduce function
   - Sorting approach
   - Recursive approach

2. [Second Largest Number](arrays/second_largest.py)
   - Using set and sorting
   - Two-pointer technique
   - Heap-based approach
   - Binary search approach

3. [Remove Duplicates](arrays/remove_duplicates.py)
   - Using set
   - Dictionary approach
   - Two-pointer technique
   - List comprehension

4. [Merge Sorted Lists](arrays/merge_sorted_lists.py)
   - Two-pointer technique
   - Using heapq
   - Recursive approach
   - Built-in sorting
   - K-way merge

5. [Most Frequent Element](arrays/most_frequent.py)
   - Using Counter
   - Dictionary counting
   - Sorting approach
   - Set operations
   - Frequency analysis

6. [Pair Sum](arrays/pair_sum.py)
   - Two-pointer technique
   - Hash set approach
   - Binary search
   - Dictionary method
   - Detailed pair analysis

### String Manipulation (`strings/`)
1. [Reverse String](strings/reverse_string.py)
   - Multiple approaches including slicing, loop, and recursion
   - Time/Space complexity analysis
   - Performance comparison

2. [Palindrome Check](strings/is_palindrome.py)
   - Two-pointer technique
   - String reversal
   - Recursive approach
   - Advanced options (case-insensitive, ignore spaces)

3. [Anagram Check](strings/is_anagram.py)
   - Sorting approach
   - Character counting
   - Dictionary-based
   - XOR operation
   - Using Counter class

4. [Count Vowels](strings/count_vowels.py)
   - Using set
   - Regular expressions
   - Loop counting
   - Filter function
   - Detailed vowel analysis

### Mathematical Problems (`math/`)
1. [Factorial Calculation](math/factorial.py)
   - Recursive approach
   - Iterative approach
   - Using reduce
   - Math module
   - Error handling

2. [Fibonacci Sequence](math/fibonacci.py)
   - Iterative approach
   - Recursive approach
   - Dynamic programming
   - Generator function
   - Matrix exponentiation

3. [Prime Number Check](math/is_prime.py)
   - Basic trial division
   - Optimized trial division
   - Sieve of Eratosthenes
   - Miller-Rabin test
   - Fermat test

4. [Sum of Digits](math/sum_digits.py)
   - String conversion
   - Mathematical approach
   - Recursive method
   - Using reduce
   - Detailed digit analysis

### Dynamic Programming (`dynamic_programming/`)
1. [Longest Common Subsequence](dynamic_programming/longest_common_subsequence.py)
   - Dynamic programming approach
   - Recursive solution
   - Memoization
   - Space-optimized version
   - Using itertools

### Searching and Sorting (`searching_sorting/`)
1. [Binary Search](searching_sorting/binary_search.py)
   - Iterative approach
   - Recursive approach
   - Using bisect module
   - Custom comparator
   - Finding insertion point

### Object-Oriented Programming (`oop/`)
1. [Person Class Implementation](oop/person_class.py)
   - Basic class structure
   - Property decorators
   - Magic methods
   - Class methods and static methods
   - Inheritance example

## Features of Each Implementation
- Multiple solution approaches
- Time and space complexity analysis
- Detailed explanations and comments
- Example usage with test cases
- Performance comparisons
- Edge case handling
- Bonus analysis functions

## How to Use
1. Each file contains multiple implementations of the same problem
2. Run any file directly to see examples and performance comparisons:
   ```bash
   python3 category/filename.py
   ```
3. Each implementation includes:
   - Problem statement
   - Example input/output
   - Time/Space complexity
   - Explanation of the approach
   - Test cases including edge cases

## Best Practices Demonstrated
- Clean, readable code
- Proper documentation
- Error handling
- Performance optimization
- Multiple solution approaches
- Test cases and edge cases
- Object-oriented principles
- Python-specific features and idioms

## Common Interview Topics Covered
- Algorithm complexity
- Data structures
- String manipulation
- Array operations
- Mathematical problems
- Recursion
- Dynamic programming
- Object-oriented programming
- Python-specific features
- Performance optimization

## Contributing
Feel free to add more questions, improve existing solutions, or suggest better approaches! 