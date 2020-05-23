from functools import reduce

a = ((lambda x: x + 2)(x) for x in range(1, 6))
for i in a:
    print(i)

l1 = [(1, 2), (2, 3), (3, 1), (6, 2), (9, 1)]
l1.sort(key=lambda x: x[1])
print(l1)

print('map example:')
# l2是map object，不能直接print
l2 = map(lambda x: x+2, [1, 2, 3, 4, 5])
print(type(l2))
for i in l2:
    print(i)

print('filter example:')
l3 = [(1, 2), (2, 3), (3, 1), (6, 2), (9, 1)]
l4 = filter(lambda x: x[1] > x[0], l3)
print(type(l4))
for i in l4:
    print(i)

print('reduce example:')
l5 = (10, 20, 30, 40)
l6 = reduce(lambda x, y: x + y, l5)
print(type(l6))
print(l6)












