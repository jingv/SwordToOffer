#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p271二叉树的深度.py
@Time    :   2018/12/17 10:39:04
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''
from Tree import Tree


def tree_depth(tree_root):
    if tree_root is None:
        return 0

    left_depth = tree_depth(tree_root.lchild)
    right_depth = tree_depth(tree_root.rchild)

    return (left_depth + 1) if left_depth > right_depth else (right_depth + 1)


def is_balanced_tree(tree_root):
    # 判读是否是平衡二叉树
    if tree_root is None:
        return True

    left_depth = tree_depth(tree_root.lchild)
    right_depth = tree_depth(tree_root.rchild)
    differ = abs(left_depth - right_depth)
    if differ <= 1:
        return True
    else:
        return False

    return is_balanced__tree(tree_root.lchild) and\
        is_balanced__tree(tree_root.rchild)


def main():
    tree = Tree()
    for i in range(11):
        tree.add(i)
    print(tree_depth(tree.root))
    print(is_balanced_tree(tree.root))


if __name__ == '__main__':
    main()
