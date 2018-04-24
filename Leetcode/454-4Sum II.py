from collections import defaultdict

def fourSumCount(A, B, C, D):
    dictAB, dictCD = defaultdict(int), defaultdict(int)

    # Keep track of number of ways to create create each sum in A, B
    # O(n^2)
    for i in A:
        for j in B:
            dictAB[i+j] += 1

    # Keep track of number of ways to create create each sum in C, D
    # O(n^2)
    for m in C:
        for n in D:
            dictCD[m+n] += 1

    count = 0

    # Iterate over the sums of A/B, and look for inberse in sums of C/D
    # O(n)
    for k in dictAB.keys():
        if -k in dictCD:
            # Multiply to get all possibilites
            count += (dictAB[k] * dictCD[-k])

    return count

# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
A = [-1,-1]
B = [-1,1]
C = [-1,1]
D = [1,-1]
print(fourSumCount(A,B,C,D))
