from itertools import accumulate
import operator

a = [1,2,3,5,4]
#acc = accumulate(a)
acc = accumulate(a, func=max)

print(a)
print(list(acc))

