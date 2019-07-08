def test_str():
	str = '*-'
	print(str.center(10, '!'))
	str2 = 'abc,defg, hij'
	print(str2.capitalize())
	print(str.rjust(10,'0'))
	print(str.ljust(10,'1'))
	str3 = '0123456789'
	print(str3[:])
	# 前闭后开，包含index=1，不含index = 3
	print(str3[1:3])
	print(str3[1:])
	print(str3[:3])
	print(str3[3:1:-1])


def test_list():
	l = [1,2,3,4,5]
	print(l*3)
	l2 = l * 2
	print(l2)
	print(l2[2])
	l2[3] = 666
	print(l2)
	l2.append(999)
	print(l2)
	# remove and return the last (not first) item
	t = l2.pop()
	print(t)
	print(l2)
	# insert into the index = 2 with value = 123
	l2.insert(2,123)
	print(l2)
	l2 += [234,567]
	# add to the last
	print(l2)
	l3 = [0,1,2,3,4,5,6,7,8,9]
	# list slice action
	print(l3[7:1:-2])
	l4 = ['a','bc','sdf','SDF','sdfD']
	for i in l4:
		print(i.title(), end= '')


import sys


def test_gen():
	g = [(x, y) for x in 'abcd' for y in range(1,6)]
	# 264
	print(sys.getsizeof(g))
	# [('a', 1), ('a', 2), ('a', 3), ('a', ...
	print(g)
	# <class 'list'>
	print(type(g))
	
	g2 = ((x, y) for x in 'abcd' for y in range(1,6))
	# 120
	print(sys.getsizeof(g2))
	# <generator object test_gen.<locals>.<genexpr> at 0x000001AEF4D40840>
	print(g2)
	# ('a', 1)
	print(next(g2))
	# ('a', 2)
	print(next(g2))
	# 120
	print(sys.getsizeof(g2))
	# <class 'generator'>
	print(type(g2))
	

def fib_gen(n:'int'):
	x, y = 0, 1
	for i in range(n):
		x, y = y, x + y
		yield x


def test_set():
	l1 = {1,2,3,4}
	l2 = {3,4,5,6}
	print('SET operating')
	print(l1.intersection(l2))
	print(l1.symmetric_difference(l2))
	print(l1.union(l2))
	print(l1.difference(l2))

	
if __name__ == '__main__':
	# test_str()
	# test_list()
	# test_gen()
	for i in fib_gen(10):
		print(i, end = ',')
	print()
	# <class 'int'>
	print(type((1)))
	# <class 'tuple'>
	print(type((1,)))
	print((1,2,3,4,5)[1:3])
	test_set()
	