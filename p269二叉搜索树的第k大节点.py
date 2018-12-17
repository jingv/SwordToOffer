#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p269二叉搜索树的第k大节点.py
@Time    :   2018/12/17 09:54:12
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''
from Tree import Tree


def kth_node(tree_root, k):
    result = None
    if tree_root.lchild is not None:
        result = kth_node(tree_root.lchild, k)
    
    if result is None:
        if k == 1:
            result = tree_root.item
        k -= 1
    
    if result is None and tree_root.rchild is not None:
        result = kth_node(tree_root.rchild, k)
    
    return result


def main():
    tree = Tree()
    k = eval(input('输入k的值：'))
    num_li = [5, 3, 7, 2, 4, 6, 8]
    for i in num_li:
        tree.add(i)
    tree.inner_travel(tree.root)
    print(kth_node(tree.root, k))


if __name__ == '__main__':
    main()
