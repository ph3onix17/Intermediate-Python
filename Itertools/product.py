from itertools import product

a = [1,2]
b = [3,4]
pro = product(a,b, repeat=2)

print(list(pro))