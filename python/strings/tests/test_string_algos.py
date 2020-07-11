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

    string = "abcdefghijklmnopqrstuvwxyz"*10
    longestSubstring = ss.longestNoneRepeatingChars(string)
    assert(longestSubstring == "abcdefghijklmnopqrstuvwxyz")


def test_rabinKarp():
    ss = SubstringSearch()
    
    string = "aaaabcddddd"
    substring = "abc"
    answer = ss.rabinKarp(string, substring)
    assert(answer == True)

    string = "aaaabcddddd"
    substring = "d"
    answer = ss.rabinKarp(string, substring)
    assert(answer == True)

    string = "aaaabcddddd"
    substring = "abcde"
    answer = ss.rabinKarp(string, substring)
    assert(answer == False)

    string = ""
    substring = "ab"
    answer = ss.rabinKarp(string, substring)
    assert(answer == False)

    string = "fjaoiebnlsnvpowefnlakvoaiepfcjelsfmefianew"
    substring = "voaie"
    answer = ss.rabinKarp(string, substring)
    assert(answer == True)

    string = "fjaoiebnlsnvpowefnlakvoaiepfcjelsfmefianew"
    substring = "w"
    answer = ss.rabinKarp(string, substring)
    assert(answer == True)

    string = ("abc"*100) + "fjaoiebnlsnvpowefnlakvoaiepfcjelsfmefianew" + ("abd"*100)
    substring = "fjaoiebnlsnvpowefnlakvoaiepfcjelsfmefianew"
    answer = ss.rabinKarp(string, substring)
    assert(answer == True)