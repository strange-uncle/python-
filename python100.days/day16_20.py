import heapq
import itertools


a = ['a', 'b', 'c', 'd']
b = [1, 2, 3]
c = [[None] * len(b)] * len(a)
d = [[None] * len(b) for i in range(len(a))]

print(c)
print(d)

e = [1,2,3,0,9,8,7,4,5,6]
print(heapq.nlargest(3, e))
print(heapq.nsmallest(2, e))

f = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(2, f, key=lambda x: x['price']))

print(list(itertools.product(a, b)))
print(list(itertools.permutations('123')))
print(list(itertools.combinations('123456', 2)))

item1 = list(map(lambda x: x*3, filter(lambda x: x % 3 == 0, range(10))))
print(item1)

