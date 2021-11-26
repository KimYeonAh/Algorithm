def all_permutations(data) :
    bUsed = [False] * len(data)
    DFS_permutation(data, [], 0, bUsed)

all_permutations(['A', 'B', 'C'])

from itertools import permutations
print(list(permutations(['A', 'B', 'C'])))
