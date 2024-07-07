from collections import Counter
'''
print(Counter([1,2,3,4,5,6,7,7,7]))

print(Counter({'A' : 5, 'B' : 2, 'C' : '3'}))

vars = Counter(a = 20, b = 30, c = 40, d = 60)
print(vars)

# a = [4,2,5,1,9,7]
# a.sort()
# print(a)

'''
# we can count how many same charactors in this 'vars' String variable using Counter
vars = 'chathuramaheshdharmasiri'

varsCounter = Counter(vars)

print(varsCounter)
print()
print(varsCounter.items())
print()
print(varsCounter.keys()) #like dictionary keys
print()
print(varsCounter.values()) #like dictionary values
print()
print(varsCounter.most_common(3)) #most common elemets with range (from 1)
print()
print(varsCounter.most_common(1)[0][0])
print()
print(list(varsCounter.elements())) #bruh this is frrrrrrrr

