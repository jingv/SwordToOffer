from Tree import Tree


def print_tree_by_level(item):
    if item.root is None:
        return
    queue = [item.root]
    # 记录下一层需要打印的数目
    next_level = 0
    # 当前还需要打印的数目
    to_be_print = 1
    while queue:
        cur = queue.pop(0)
        to_be_print -= 1
        print(cur.item, end=' ')
        if cur.lchild is not None:
            queue.append(cur.lchild)
            next_level += 1
        if cur.rchild is not None:
            queue.append(cur.rchild)
            next_level += 1
        if to_be_print == 0:
            print()
            to_be_print = next_level
            next_level = 0


def main():
    tree = Tree()
    for i in range(1, 16):
        tree.add(i)
    # tree.breath_travel()
    print_tree_by_level(tree)


if __name__ == '__main__':
    main()
