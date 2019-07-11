from time import sleep
from abc import ABCMeta, abstractmethod


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        print('%s hour(s) %s minute(s) %s second(s)' % (self._hour, self._minute, self._second))


class TestProperty(object):
    
    __slots__ = ('_name', '_age', '_gender')
    
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
    
    @staticmethod
    def static_check_gender(gender):
        return False if gender not in {'M', 'F'} else True
        
    def show(self):
        print('name is %s and age is %s' % (self._name, self._age))


class Pet(object, metaclass=ABCMeta):
    def __init__(self, name: 'str'):
        self._name = name
    
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def run(self):
        pass


# pycharm 右键点击Dog -> 生成->实现方法, 可以看到所有需要实现的 抽象方法abstract method
class Dog(Pet):
    def run(self):
        print('%s is running fast' % self._name)

    def speak(self):
        print('%s 汪汪汪' % self._name)


class Pig(Pet):
    
    def speak(self):
        print('%s 哼唧哼唧' % self._name)

    def run(self):
        print('%s is running slow' % self._name)


if __name__ == '__main__':
    # c = Clock(23, 58, 23)
    # while True:
    #    c.show()
    #    sleep(1)
    #    c.run()
    p = TestProperty('abc', 16)
    p.show()
    p.age = 123
    p.show()
    # p.name = '6' AttributeError: can't set attribute
    p._gender = 'M'
    # p._height = 180 AttributeError: 'test_property' object has no attribute '_height'
    print(TestProperty.static_check_gender('M'))
    print(TestProperty.static_check_gender('F'))
    print(TestProperty.static_check_gender('MF'))
    d1 = Dog('嘟嘟')
    p1 = Pig('佩奇')
    # 多态 polymorphism
    d1.run()
    p1.run()
    d1.speak()
    p1.speak()