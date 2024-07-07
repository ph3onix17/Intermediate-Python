from itertools import combinations,combinations_with_replacement

a = [1,2,3,4]
com = combinations(a,2)

print(list(com))

comwr = combinations_with_replacement(a,2)
print(list(comwr))

