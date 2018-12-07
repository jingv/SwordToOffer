# coding:utf-8
class Stack(object):
    """定义一个栈"""
    def __init__(self):
        self.__queue = []

    def len(self):
        return len(self.__queue)

    def add(self, item):
        self.__queue.append(item)

    def pop(self):
        if len(self.__queue) == 0:
            return None
        else:
            return self.__queue.pop()


class Queue(object):
    """定义一个队列"""
    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack()

    def add_push(self, item):
        self.__stack1.add(item)

    def pop_head(self):
        if self.__stack2.len() != 0:
            return self.__stack2.pop()
        else:
            while self.__stack1.len() != 0:
                self.__stack2.add(self.__stack1.pop())
            return self.__stack2.pop()

    def len(self):
        return self.__stack1.len() + self.__stack2.len()


def main():
    queue = Queue()
    for i in range(1, 11):
        queue.add_push(i)
    print(queue.pop_head())
    for i in range(11, 16):
        queue.add_push(i)
    while queue.len() != 0:
        print(queue.pop_head())


if __name__ == '__main__':
    main()
