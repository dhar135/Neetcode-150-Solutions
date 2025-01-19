from src.arrays_and_hashing.duplicate_integer import has_duplicate

def test_has_duplicate():

    assert has_duplicate([1, 2, 3, 3]) is True
    assert has_duplicate([1, 2, 3, 4]) is False