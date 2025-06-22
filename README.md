# Python Interview Practice Questions

This repository contains a collection of commonly asked Python interview questions with multiple solution approaches, detailed explanations, and performance comparisons.

## Questions Covered

Below is a comprehensive, deduplicated list of all coding questions solved in this repository, grouped by topic. Each question is implemented in multiple ways and can be found in the referenced file.

### String-Based Questions
1. Reverse a string — without using built-ins ([strings/reverse_string.py](strings/reverse_string.py))
2. Is it a palindrome? ([strings/is_palindrome.py](strings/is_palindrome.py))
3. Remove duplicates from a string — efficiently ([strings/remove_duplicates.py](strings/remove_duplicates.py))
4. First non-repeating character ([strings/first_non_repeating.py](strings/first_non_repeating.py))
5. Count how many times each character appears ([strings/character_frequency.py](strings/character_frequency.py))
6. Flip the words in a sentence, not the letters ([strings/reverse_words.py](strings/reverse_words.py))
7. Are two strings anagrams? ([strings/is_anagram.py](strings/is_anagram.py))
8. Longest substring without repeats — sliding window style ([strings/longest_substring_without_repeats.py](strings/longest_substring_without_repeats.py))
9. Build your own atoi — string to integer ([strings/atoi.py](strings/atoi.py))
10. Compress strings with run-length encoding ([strings/run_length_encoding.py](strings/run_length_encoding.py))
11. Most frequent character ([strings/most_frequent_character.py](strings/most_frequent_character.py))
12. List all possible substrings of a string ([strings/all_substrings.py](strings/all_substrings.py))
13. Is one string a rotation of another? ([strings/is_rotation.py](strings/is_rotation.py))
14. Strip all white spaces from a string ([strings/strip_whitespace.py](strings/strip_whitespace.py))
15. Is this a valid shuffle of two strings? ([strings/valid_shuffle.py](strings/valid_shuffle.py))
16. Convert text to Title Case — properly ([strings/title_case.py](strings/title_case.py))
17. Find the longest common prefix among words ([strings/longest_common_prefix.py](strings/longest_common_prefix.py))
18. Break a string into a char array ([strings/to_char_array.py](strings/to_char_array.py))
19. Replace spaces with %20 — classic URL trick ([strings/replace_spaces.py](strings/replace_spaces.py))
20. Turn full sentences into acronyms ([strings/acronym.py](strings/acronym.py))
21. Check if the string is all digits ([strings/is_all_digits.py](strings/is_all_digits.py))
22. Count how many words are in the string ([strings/word_count.py](strings/word_count.py))
23. Remove a specific character ([strings/remove_character.py](strings/remove_character.py))
24. Find the shortest word in a sentence ([strings/shortest_word.py](strings/shortest_word.py))
25. Longest palindromic substring — two-pointer style ([strings/longest_palindromic_substring.py](strings/longest_palindromic_substring.py))

### Array-Based Questions
26. Reverse an array in-place ([arrays/reverse_array.py](arrays/reverse_array.py))
27. Find the largest element ([arrays/find_max.py](arrays/find_max.py))
28. Find the second largest element ([arrays/second_largest.py](arrays/second_largest.py))
29. Check for duplicates in an array ([arrays/check_duplicates.py](arrays/check_duplicates.py))
30. Remove duplicates — return only unique values ([arrays/remove_duplicates.py](arrays/remove_duplicates.py))
31. Find the missing number from 1 to N ([arrays/find_missing_number.py](arrays/find_missing_number.py))
32. Move all zeros to the end — keep order ([arrays/move_zeros.py](arrays/move_zeros.py))
33. Rotate the array left/right by K positions ([arrays/rotate_array.py](arrays/rotate_array.py))
34. Find the Kth largest/smallest element ([arrays/kth_element.py](arrays/kth_element.py))
35. Merge two sorted arrays — without using extra space ([arrays/merge_sorted_lists.py](arrays/merge_sorted_lists.py))
36. Find the intersection of two arrays ([arrays/intersection.py](arrays/intersection.py))
37. Sort 0s, 1s, and 2s without using sort() ([arrays/sort_012.py](arrays/sort_012.py))
38. Find subarrays with a given sum ([arrays/subarrays_with_sum.py](arrays/subarrays_with_sum.py))
39. Detect if a subarray sums to 0 ([arrays/detect_zero_sum_subarray.py](arrays/detect_zero_sum_subarray.py))
40. Find the longest increasing subsequence ([arrays/longest_increasing_subsequence.py](arrays/longest_increasing_subsequence.py))
41. Kadane's Algorithm — maximum subarray sum ([arrays/kadane_max_subarray.py](arrays/kadane_max_subarray.py))
42. Check if array is sorted and rotated ([arrays/is_sorted_and_rotated.py](arrays/is_sorted_and_rotated.py))
43. Rearrange array in max-min order alternately ([arrays/max_min_rearrange.py](arrays/max_min_rearrange.py))
44. Find leaders in an array (no greater element to the right) ([arrays/leaders.py](arrays/leaders.py))
45. Calculate frequency of all elements in O(n) ([arrays/frequency_count.py](arrays/frequency_count.py))
46. Product of all elements except self ([arrays/product_except_self.py](arrays/product_except_self.py))

### Other Topics
- Factorial calculation ([math/factorial.py](math/factorial.py))
- Fibonacci sequence ([math/fibonacci.py](math/fibonacci.py))
- Prime number check ([math/is_prime.py](math/is_prime.py))
- Sum of digits ([math/sum_digits.py](math/sum_digits.py))
- Longest common subsequence ([dynamic_programming/longest_common_subsequence.py](dynamic_programming/longest_common_subsequence.py))
- Binary search ([searching_sorting/binary_search.py](searching_sorting/binary_search.py))
- Person class implementation ([oop/person_class.py](oop/person_class.py))

## How to Use
Each file contains multiple implementations of the same problem. Run any file directly to see examples and performance comparisons:

```bash
python3 category/filename.py
```

## Notes
- All questions are unique and deduplicated.
- Each solution includes multiple approaches, time/space complexity, and example usage.
- For any question, see the referenced file for details and code.

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

## Features of Each Implementation
- Multiple solution approaches
- Time and space complexity analysis
- Detailed explanations and comments
- Example usage with test cases
- Performance comparisons
- Edge case handling
- Bonus analysis functions

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