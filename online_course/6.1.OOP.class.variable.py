# class内部的变量如果是两个下划线开头并且是两个下划线结尾,例如 __a__
# 就是特殊的变量,外部可以访问,只是需要注意这些变量可能是有特殊用途的.

# 如果某个class的变量是两个下划线开头,结尾没有下划线,类似 __a,
# 那么这个变量就是严格意义上类的私有变量,可以认为外部不能访问,强制访问会报错.
# 但实际上,外部有一些投机取巧的方法可以访问.

# 如果某个class的变量是一个下划线开头,结尾没有下划线,类似 _a,
# 以及下面我用的stu._name
# 意思是这种变量可以认为是类的内部变量,虽然在外部访问,但最好不要这样做.
# 尽量通过OO的方式来操作数据.


class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    __sex = 'secret'

    def print_score(self):
        print('Class function, score is %s' % (self._score,))


stu = Student('tom', 66)
print(stu._name, stu._score)
stu.print_score()

# stu.__sex是内部变量,访问会报错
# print(stu.__sex)


# 访问了类的私有变量__sex,但不建议这样搞.
print(stu._Student__sex)




