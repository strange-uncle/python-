# 省略判断条件，这不是一个好的实践，最好是写完整.

# 空的字符串会被解析成为False，其他的就都是True
s1 = 'abc'
s2 = ''
if s1:
    print(f's1 comes into IF with value {s1}')

if s2:
    print(f's2 comes into IF with value {s2}')
elif not s2:
    print(f's2 NOT comes into IF with value {s2}')

# 数字0会被解析成False，其他的都是True
i1 = 1
i0 = 0
if i1:
    print(f'i1 comes into IF with value {i1}')
# 空的字符串会被解析成为False，其他的就都是True
if i0:
    print(f'i0 comes into IF with value {i0}')
elif not s2:
    print(f'i0 NOT comes into IF with value {i0}')

dic = {'a':1, 'b':2, 'c':3, 'd':4}
for k,v in dic.items():
    print(f'k is {k} and v is {v}\n')

# 这里的i是tuple
for i in dic.items():
    print(f'item is {i} and type is {type(i)}\n')

for v in dic.values():
    print(f'v in dic.values() is {v}\n')

st = {1,2,3,4,5,6}
for i in st:
    print(f'value in the set is {i}')

# 不能通过下表来访问set
# print(st[2])

for i,v in enumerate(st):
    print(f'enumerate from set, index is {i} and value is {v}')

for i in list(st):
    print(f'list from set, item is {i}')


