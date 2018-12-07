from Tree import Tree


def search_path(item, sum_num, path=[]):
    if item is None:
        return
    path.append(item.item)
    # 遍历当前节点的左右子树
    if item.lchild is not None:
        # path.append(item.lchild.item)
        search_path(item.lchild, sum_num, path)
    if item.rchild is not None:
        # path.append(item.rchild.item)
        search_path(item.rchild, sum_num, path)
    # 当前节点为叶子节点的情况
    if item.lchild is None and item.rchild is None:
        if sum(path) == sum_num:
            for i in path:
                print(i, end=' ')
            print()
    # 弹出当前节点
    path.pop()


def main():
    tree = Tree()
    for i in [10, 5, 10, 4, 7, 0, 1, 0, 0, 1, 0, 2, 3, 3, 1]:
        tree.add(i)
    # tree.breath_travel()
    search_path(tree.root, 22)


if __name__ == '__main__':
    main()
