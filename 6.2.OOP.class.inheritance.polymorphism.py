# inheritance and polymorphism
# 继承和多态
from enum import Enum, unique, IntEnum


class Animal(object):

    # 父类__slots__的约束对子类无效
    __slots__ = ('__name', '__score', 'test_variable1')

    def __init__(self, name):
        self.__name = name
        self.__score = 0
        # init里面加的属性 也会违背自身的__slots__
        # 会报错
        # self.__sex = 'M'

    # 把方法转成属性来方便调用
    @property
    def score(self):
        return self.__score

    # 注意,是name.setter,不是property.setter
    @score.setter
    def score(self, value):
        if isinstance(value, int):
            self.__score = value
        else:
            raise TypeError


class RunnableMixIn(object):
    def run(self):
        print('running')


class FlyableMixIn(object):
    def fly(self):
        print('Flying')


# Person继承了父类的__init__和score getter & setter
# 同时也继承了RunnableMixIn的run
class Person(Animal, RunnableMixIn):
    pass


a1 = Animal('a1')
a1.test_variable1 = 'check slots'
print(a1.test_variable1)

# 如下验证slots的约束
# AttributeError: 'Animal' object has no attribute 'test_variable2'
# a1.test_variable2 = 'check slots 2'


p1 = Person('adf')

# 父类__slots__的约束对子类无效
# 所以这里不报错
p1.test_variable2 = 'check slots 2'


print(p1.score)
p1.run()

# 如下不满足检查条件,会报错
# p1.score = 'ab'

p1.score = 99

print(p1.score)


# 测试继承的情况下,方法覆盖
def run():
    print('new function is running')


p1.run = run

# 这个会调用子类上面添加的方法:new function is running
p1.run()

del p1.run
# 这个会调用父类的方法:running
p1.run()


# 枚举类
# @unique保证没有重复,比如定义一个A = 3,就会报错:
# ValueError: duplicate values found in <enum 'Weekday'>: A -> Wednesday
# 如果不加@unique, 那么A = 3就不会报错
@unique
class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


# IntEnum 限制了value必须是数字,或者能够转换成为数字,比如'123'这个就可以
class WeekdayInt(IntEnum):
    Monday = 1
    Tuesday = '2'
    # ValueError: invalid literal for int() with base 10: '3b'
    # Wednesday = '3b'


