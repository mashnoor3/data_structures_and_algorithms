# 242. Valid Anagram

from collections import defaultdict

def isAnagram(s,t):
    if len(s) != len(t):
        return False

    dict_s = defaultdict(int)
    dict_t = defaultdict(int)

    for letter in s:
        dict_s[letter] += 1
    for letter in t:
        dict_t[letter] += 1

    for k in dict_s.keys():
        if not(dict_s[k]==dict_t[k]):
            return False
    return True

isAnagram("mashnoor","rhonhsam")
