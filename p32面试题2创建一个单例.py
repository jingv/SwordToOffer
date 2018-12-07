# coding:utf-8


class Dog(object):
    _instance = None

    def __new__(cls, name):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    a = Dog('旺财')
    b = Dog('哮天犬')
    print(id(a))
    print(id(b))
