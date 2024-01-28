def permutation(orig_list) -> list:
    length = len(orig_list)
    perm_list = []
    if length <=1:
        return [orig_list]
    for i in range (0, length):
        item = orig_list[i]
        remains = orig_list[:i] + orig_list[(i+1):]
        for p in permutation(remains):
            perm_list.append([item] + p)
    return perm_list
#print(permutation([0,1,2,3,4,5,6,7,8]))

from itertools import permutations
print(list(permutations(list(range(0,10)))))
"""for i in permutations(['a','b','c']):
    print(i[0])"""