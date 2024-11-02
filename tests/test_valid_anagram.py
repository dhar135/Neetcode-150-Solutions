from src.arrays_and_hashing.valid_anagram import valid_anagram

def test_valid_anagram():
    assert valid_anagram("racecar", "carrace") == True
    assert valid_anagram("jar", "jam") == False
    assert valid_anagram("jam", "jamm") == False
