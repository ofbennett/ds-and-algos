import pytest
from .. import SubstringSearch

def test_longestNoneRepeatingChars():
    ss = SubstringSearch()
    
    string = "aaaabcddddd"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "abcd")

    string = "aaaaaaaaabaaaaaaadcbaaa"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "adcb")

    string = "a"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "a")

    string = ""
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "")

    string = "abcddddd"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "abcd")

    string = "aaaaaaabcd"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "abcd")

    string = "aaaaaaab"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "ab")

    string = "ababababab"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "ab")

    string = "aaabbbaaaa"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "ab")

    string = "abcdefghijklmnopqrstuvwxyz"
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "abcdefghijklmnopqrstuvwxyz")

    string = "abcdefghijklmnopqrstuvwxyz"*100
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "abcdefghijklmnopqrstuvwxyz")