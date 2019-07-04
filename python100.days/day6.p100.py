from random import randint
from temp.test_import import foo

def add_int(*n: 'int'):
	s = 0
	for i in n:
		s += i
	return s

print(add_int(1))
print(add_int(1,2))
print(add_int(1,2,3))

foo()

# 最大公约数
def greatest_common_divisor(a: 'int', b: 'int'):
	if a > b:
		a, b = b, a
	for i in range(a, 0 , - 1):
		if a % i == 0 and b % i == 0:
			return i
	return None

print('gcd of %i and %i is %i' % (3, 15, greatest_common_divisor(6, 18)))
print('gcd of %i and %i is %i' % (3, 6, greatest_common_divisor(3, 6)))
print('gcd of %i and %i is %i' % (3, 6, greatest_common_divisor(7, 13)))

# 最小公倍数
# 关于最小公倍数lcm 与 最大公约数gcd，我们有这样的定理：lcm * gcd = a * b
def lowest_common_multiple(a: 'int', b: 'int'):
	return a*b/greatest_common_divisor(a, b)

print('lowest common multiple of %i and %i is %i' % (3,6,lowest_common_multiple(3, 6)))
print('lowest common multiple of %i and %i is %i' % (5,7,lowest_common_multiple(5, 7)))


def is_palindromic_number(n: 'str'):
	min = 0
	max = len(n) - 1
	while min < max:
		if n[min] == n[max]:
			min += 1
			max -= 1
			continue
		print('%s is NOT palindromic number' % n)
		return
	print('%s is palindromic number' % n)


is_palindromic_number('1234567')
is_palindromic_number('1234567654321')
is_palindromic_number('226699')
is_palindromic_number('223322')
