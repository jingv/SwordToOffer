# coding:utf-8
from SingleLinkList import SingleLinkList

"""
    用栈可以解决的问题，就可以使用递归来解决这个问题。 递归在本质上就是一个栈结构
     使用递归的时候注意栈溢出的问题。
"""

def print_item_reverse(single_link_list):
    if not single_link_list.isEmpty():
        print(single_link_list.pop())
        print_item_reverse(single_link_list)


if __name__ == '__main__':
    single_link_list = SingleLinkList()
    for i in range(1, 11):
        single_link_list.append(i)
    print_item_reverse(single_link_list)
