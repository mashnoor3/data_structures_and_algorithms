def firstUniqChar(s):
    from collections import defaultdict
    dict = defaultdict(int)
    for letter in s:
        dict[letter] += 1
    for i, letter in enumerate(s):
        if dict[letter] == 1:
            return i
    return -1
