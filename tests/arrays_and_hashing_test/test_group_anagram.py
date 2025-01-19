from src.arrays_and_hashing.group_anagram import Solution

def test_group_anagrams():
    solution = Solution()
    
    # Test 1
    result1 = solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    print("Test 1 Input: ['act', 'pots', 'tops', 'cat', 'stop', 'hat']")
    print("Test 1 Expected Output: [['hat'], ['act', 'cat'], ['stop', 'pots', 'tops']]")
    print("Test 1 Result:", result1)
    assert sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]])

    # Test 2
    result2 = solution.groupAnagrams(["x"])
    print("\nTest 2 Input: ['x']")
    print("Test 2 Expected Output: [['x']]")
    print("Test 2 Result:", result2)
    assert result2 == [["x"]]

    # Test 3
    result3 = solution.groupAnagrams([""])
    print("\nTest 3 Input: ['']")
    print("Test 3 Expected Output: [['']]")
    print("Test 3 Result:", result3)
    assert result3 == [[""]]

    print("\nAll tests passed!")