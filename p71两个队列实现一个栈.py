# coding:utf-8
class Queue(object):
    """定义一个队列类"""
    def __init__(self):
        self.__queue = []

    def len(self):
        return len(self.__queue)

    def add(self, item):
        self.__queue.append(item)

    def pop(self):
        if not self.__queue:
            return None
        else:
            return self.__queue.pop(0)


class Stack(object):
    """创建一个栈对象"""
    def __init__(self):
        self.__queue1 = Queue()
        self.__queue2 = Queue()

    def len(self):
        return self.__queue1.len() if self.__queue1.len() else self.__queue2.len()

    def add(self, item):
        queue = self.__queue1 if self.__queue1.len() else self.__queue2
        queue.add(item)

    def pop(self):
        if self.__queue1.len() or self.__queue2.len():
            if self.__queue1.len():
                while self.__queue1.len() > 1:
                    self.__queue2.add(self.__queue1.pop())
                return self.__queue1.pop()
            else:
                while self.__queue2.len() > 1:
                    self.__queue1.add(self.__queue2.pop())
                return self.__queue2.pop()
        return None

if __name__ == '__main__':
    # queue = Queue()
    # for i in range(1, 11):
    #     queue.add(i)
    # print(queue.len())
    # while queue.len():
    #     print(queue.pop())
    stack = Stack()
    stack.add(1)
    stack.add(2)
    stack.add(3)
    stack.add(4)
    print('========')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.len())
