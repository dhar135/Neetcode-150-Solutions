"""
Problem: Duplicate Integer
Difficulty: Easy
Link: https://neetcode.io/problems/duplicate-integer

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]
Output: true

Example 2:

Input: nums = [1, 2, 3, 4]
Output: false

Approach:
- Create a set.
- Loop through the array and check if the number is in the map.
- If the element appears more than once, return true.

Time Complexity: O(n)
Space Complexity: O(n)

"""
from typing import List


def has_duplicate(nums: List[int]) -> bool:

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False