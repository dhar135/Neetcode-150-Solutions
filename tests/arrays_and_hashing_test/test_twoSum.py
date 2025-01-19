from src.arrays_and_hashing.twoSum import twoSum

def test_two_sum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3,3], 6) == [0, 1]
    assert twoSum([3,4,5,6], 7) == [0, 1]
    assert twoSum([4,5,6], 10) == [0, 2]
