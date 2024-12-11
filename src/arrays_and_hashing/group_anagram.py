"""
Problem: Groups Anagrams
Difficulty: Medium
Link: https://neetcode.io/problems/anagram-groups

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
- Input: strs = ["act","pots","tops","cat","stop","hat"]
- Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
- Input: strs = ["x"]
- Output: [["x"]]

Example 3:
- Input: strs = [""]
- Output: [[""]]

Constraints:
- 1 <= strs.length <= 1000.
- 0 <= strs[i].length <= 100
- strs[i] is made up of lowercase English letters.

1st Approach:
- Iterate through strings
- Create signatures
- group signatures

Time Complexity: O(n * n log n)
Space Complexity: O(m * n)

2nd Approach:
- Create a dictionary
- Iterate through strings
- count frequencies of
- Convert count array to tuple to make it hashable

Time Complexity: O(m * n)
Space Complexity: O(m * n)

"""


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create res dictionary:
        res = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
            
        return list(res.values())





