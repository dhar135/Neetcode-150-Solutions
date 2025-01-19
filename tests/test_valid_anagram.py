from src.arrays_and_hashing.valid_anagram import valid_anagram

def test_valid_anagram():

    # Base Case: Are strings the same length?
    assert valid_anagram('jam', 'jamm') is False

    # Case: Invalid Anagram
    assert valid_anagram('jar', 'jam') is False

    # Case: Valid Anagram
    assert valid_anagram('racecar', 'carrace') is True

