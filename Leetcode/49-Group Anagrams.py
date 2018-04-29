# Idea is to use the sorted word as a key for the hashmap

from collections import defaultdict

def groupAnagrams(strs):
    out = defaultdict(list)
    for word in strs:
        k = genKey(word)
        out[k].append(word)
    # Formatting output to be a list
    out = [i for i in out.values()]
    return out

def genKey(word):
    s = ""
    for c in sorted(word):
        s += c
    return s
