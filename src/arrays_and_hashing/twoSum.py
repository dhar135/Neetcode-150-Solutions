"""
Problem: Two Sum
Difficulty: Easy
Link: https://neetcode.io/problems/two-integer-sum

Problem Description:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

Approach:
1. Loop Through the array
2. For each num, calculate the complement of the sum
3. Check if the complement is in the hashmap
    a) If Yes, return the indices of num and complement
    b) If No, add the num to the hashmap with its index

Time Complexity: O(n)
Space Complexity: O(n)

"""
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    prev = {} # Val : Index

    for i, num in enumerate(nums): # Step 1
        diff = target - num  # Step 2

        if diff in prev:  # Step 3
            return [prev[diff], i]
        else:
            prev[num] = i
