# coding:utf-8

from Tree import Node


def rebuild_tree(forward_list, in_list):

    if len(forward_list) == 0 or len(in_list) == 0:
        return None
    elif len(forward_list) == 1 and len(in_list) == 1:
        return Node(forward_list[0])

    in_list_index = in_list.index(forward_list[0])
    left_lenth = in_list_index

    tree = Node(forward_list[0])
    tree.lchild = rebuild_tree(forward_list[1: left_lenth+1], in_list[0: left_lenth])
    tree.rchild = rebuild_tree(forward_list[left_lenth+1:], in_list[left_lenth+1: ])

    return tree
    # right_length = len(in_list_index) - in_list_index -1


def width_travel(node):
    if node is None:
        return None
    else:
        queue = [node]
        while queue:
            cur = queue.pop(0)
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)
            print(cur.item, end=' ')


if __name__ == '__main__':
    forward_list = [1, 2, 4, 7, 3, 5, 6, 8]
    in_list = [4, 7, 2, 1, 5, 3, 8, 6]

    rtree = rebuild_tree(forward_list, in_list)

    width_travel(rtree)
