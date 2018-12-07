def is_or_not_searchtree(item):
    if len(item) == 0:
        return True
    left = 0
    # 找到左子树结束的位置
    for i in item[:-1]:
        left += 1
        if i > item[-1]:
            break
    # print(left)
    # 检查右子树是否符合二叉搜索树的标准（右子树的所有件节点的值都大于根节点）
    for j in item[left: -1]:
        if j < item[-1]:
            return False
    left_is_or_not = is_or_not_searchtree(item[:left])
    right_is_or_not = is_or_not_searchtree(item[left:-1])
    return (left_is_or_not and right_is_or_not)


def main():
    # example_list = [5, 7, 6, 9, 11, 10, 8]
    example_list = [7, 4, 6, 5]
    print(is_or_not_searchtree(example_list))
    # is_or_not_searchtree(example_list)


if __name__ == '__main__':
    main()

'''
    总结：
        在判断某个序列是否是二叉搜索树的前序或者后序遍历时：
            1、先找到根节点：前序为第一个，后序为最后一个
            2、找到左子树与右子树的分界点，即第一个大于根节点值的元素的位置
            3、判断右子树（序列除左子树与根节点的剩余部分）是否符合二叉搜索树的标准
            4、利用递归的算法，进一步进行判断
'''
