class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                else:
                    queue.append(cur.lchild)
                if cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.rchild)

    def breath_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                print(cur.item, end=' ')
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)

    def inner_travel(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inner_travel(node.lchild)
        print(node.item, end=' ')
        self.inner_travel(node.rchild)

    def forward_travel(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.item, end=' ')
        self.inner_travel(node.lchild)
        self.inner_travel(node.rchild)

    def post_travel(self, node):
        """后序遍历"""
        if node is None:
            return
        self.inner_travel(node.lchild)
        self.inner_travel(node.rchild)
        print(node.item, end=' ')


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add(i)
    tree.breath_travel()
    print()
    tree.inner_travel(tree.root)
