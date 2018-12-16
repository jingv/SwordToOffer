class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def isEmpty(self):
        return self.__head is None

    def len(self):
        lenth = 0
        if not self.isEmpty():
            cur = self.__head
            while cur is not None:
                cur = cur.next
                lenth += 1
        return lenth
    
    def insert(self, item):
        '''从头添加元素'''
        node = Node(item)
        if not self.isEmpty():
            node.next = self.__head
        self.__head = node

    def append(self, item):
        '''从尾添加元素'''
        node = Node(item)
        if not self.isEmpty():
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        else:
            self.__head = node

    def pop(self):
        '''从尾弹出元素'''
        if self.isEmpty():
            return None
        elif self.len() == 1:
            num = self.__head.item
            self.__head = None
            return num
        else:
            cur = self.__head
            while cur.next.next is not None:
                cur = cur.next
            num = cur.next.item
            cur.next = None
            return num
    
    def pop_head(self):
        '''从头弹出元素'''
        if self.isEmpty():
            return None
        num = self.__head.item
        self.__head = self.__head.next
        return num


if __name__ == '__main__':
    single_link_list = SingleLinkList()
    for i in range(1, 2):
        single_link_list.append(i)
    print(single_link_list.len())
    print(single_link_list.pop())
    print(single_link_list.len())
    print(single_link_list.pop())
