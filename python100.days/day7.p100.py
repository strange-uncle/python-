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
	# 这是set，集合
	l1 = {1,2,3,4}
	l2 = {3,4,5,6}
	# 空集合要用 set()
	l3 = set()
	# 这是创建空的元组, 后续也不能修改了
	t1 = ()
	print("type of l1 and l3: ", type(l1), type(l3))
	print("type of t1 = () : ", type(t1))
	# 这是dictionary,字典
	d1 = {'a':1, 'b':2}
	# 空字典要用花括号
	d2 = {}
	print("type of d1 and d2: ", type(d1), type(d2))
	print('SET operating')
	print(l1.intersection(l2))
	print(l1.symmetric_difference(l2))
	print(l1.union(l2))
	print(l1.difference(l2))


import os, time, random

def test_running_text():
	str = '这是一段文本，会动的文本。'
	while True:
		os.system('cls')
		print(str)
		time.sleep(0.2)
		str = str[1:] + str[0]
		
def generate_code(length: 'int' = 4) -> 'str':
	str = '0123456789abcdABCD'
	code = ''
	for i in range(length):
		code += str[random.randint(0, len(str) - 1)]
	return code


def get_filename_extension(filename: 'str') -> 'str':
	dot_index = filename.rfind('.')
	return filename[dot_index:]


def get_the_top_two_biggest(lst: 'list') -> 'tuple':
	e1, e2 = (lst[0], lst[1]) if lst[0] > lst[1] else (lst[1], lst[0])
	for i in range(2, len(lst)):
		if lst[i] > e1:
			e2 = e1
			e1 = lst[i]
		elif lst[i] > e2:
			e2 = lst[i]
	return (e1, e2)


def josephus_problem(total_person: 'int', kill_rank: 'int', kill_target: 'int'):
	""" 约瑟夫环问题
		有15个基督徒和15个非基督徒在海上遇险，
		为了能让一部分人活下来不得不将其中15个人扔到海里面去，
		有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
		他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
		由于上帝的保佑，15个基督徒都幸免于难，
		问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。

	:param total_person: 总的人数
	:param kill_rank: 第几个人被杀, index需要-1
	:param kill_target: 一共需要杀多少人
	:return: Nothing return.
	"""
	p = [0] * total_person
	counter = 0
	index = 0
	killed = 0
	while killed < kill_target:
		while counter < kill_rank:
			if p[index] == 0:
				counter += 1
			if counter == kill_rank:
				p[index] = 1
			index += 1
			index %= total_person
		counter = 0
		killed += 1
	for k, v in enumerate(p):
		print('%i person is %s' % ((k+1, 'safe.' if v == 0 else 'killed.')))
	print(p)

if __name__ == '__main__':
	"""
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
	# test_set()
	# test_running_text()

	print(generate_code())
	print(generate_code(5))
	print(generate_code(5))
	print(get_filename_extension('a.exe'))
	print(get_filename_extension('abs.txt'))
	print(get_filename_extension('.mp4'))
	print(get_the_top_two_biggest([6,6,6,6,6,6]))
	print(get_the_top_two_biggest([1,2,3,4,5,6,7,8]))
	print(get_the_top_two_biggest([5,2,7,9,1,0,666,10,9]))
	
	l = [
		['a','b','c'],[1,2,3]
	]
	l0 = l[0]
	l1 = l[1]
	print(l0)
	print(l1)
	l2 = [
		[4,5,6],[7,8,9]
	][1]
	print(l2)
	"""
	print(josephus_problem.__doc__)
	josephus_problem(13,3,9)
