from io import StringIO, BytesIO


# 常规写法,要记到调用close90
try:
    f1 = open('/home/kwu/test_IO/a','r')
    print(f1.read())
finally:
    if f1:
        f1.close()

print('简化写法')
# 简化写法,不用手动调用close()
with open('/home/kwu/test_IO/a','r') as f2:
    print(f2.read())


print('限制每次读取300 Bytes')
# 限制每次读取300 Bytes的数据
# 文件大小是1KB,所以需要跑4次
with open('/home/kwu/test_IO/a', 'r') as f3:
    data = f3.read(300)
    while data:
        print(data)
        print('------')
        data = f3.read(300)

# 读取文本文件默认是UTF-8编码
# 也可以手动指定编码
# f4 = open('/home/kwu/test_IO/a13', 'r', encoding = 'UTF-8')

# 写入文件用w, 如果文件已经存在那么会覆盖
# 用参数a就是append的意思,会作为新行最佳到文件末尾
# with open('/home/kwu/test_IO/a', 'a') as f5:
#    f5.write('here is new txt')


# 在内存里读写str
str1 = StringIO()
x = str1.write('132\n456')
# x is 7
print('x is: ', x)
# str1 is: <_io.StringIO object at 0x7f3661dd6798>
print('str1 is:', str1)
# 132
# 456
print(str1.getvalue())


