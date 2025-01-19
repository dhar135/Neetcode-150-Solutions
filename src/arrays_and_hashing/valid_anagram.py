"""
Problem: Is Anagram?
Difficulty: Easy
Link: https://neetcode.io/problems/is-anagram

Description:
- Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
- An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
- Input: s = "racecar", t = "carrace"
- Output: true

Example 2:
- Input: s = "jar", t = "jam"
- Output: false

Constraints:
- s and t consist of lowercase English letters.

Approach:
- Base Check to see if the two strings are the same length, return false if they are not.
- Initialize list counter as long as alphabet.
- Loop through letters in string an add +1 to the counter if in 's' but -1 if in 't'.
- - If the two strings are anagrams than the counter should be at 0. For Example: "aaa" and "aaa" is equivalent to 3 - 3 = 0
- Loop through each value in counter and if != 0 return False, else return True


Time Complexity: O()
Space Complexity: O()

"""

def valid_anagram(s: str, t: str) -> bool:

    # Base Check
    if len(s) != len(t):
        return False
    
    count = [0] * 26

    for i in range(len(s)):

        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True



