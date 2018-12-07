from Tree import Tree


def z_print_tree(item):
    # 之字形后者z字形打印二叉树
    if item.root is None:
        return
    level_num = 1
    to_be_print = [item.root]
    next_level = []
    while to_be_print:
        cur = to_be_print.pop()
        print(cur.item, end=' ')
        # 如果下一行是奇数行，按照先右后左的顺序入栈；如果下一行是偶数行，按照先右后左的顺序入栈
        if level_num & 1:
            if cur.lchild is not None:
                next_level.append(cur.lchild)
            if cur.rchild is not None:
                next_level.append(cur.rchild)
        else:
            if cur.rchild is not None:
                next_level.append(cur.rchild)
            if cur.lchild is not None:
                next_level.append(cur.lchild)
        # 如果下一行不存在元素，当前行全部打印完成，则退出程序
        if next_level == [] and to_be_print == []:
            break
        # 如果当前行打印完成，则将当前行的值赋值为下一行，并将下一行的值初始化为[]，同时行号+1
        if to_be_print == []:
            print()
            to_be_print = next_level
            next_level = []
            level_num += 1


def main():
    tree = Tree()
    for i in range(1, 16):
        tree.add(i)
    # tree.breath_travel()
    z_print_tree(tree)


if __name__ == '__main__':
    main()
