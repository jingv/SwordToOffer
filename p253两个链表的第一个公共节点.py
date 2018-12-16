from SingleLinkList import SingleLinkList


def find_common_node1(singlelinklistA, singlelinklistB):
    """
        思路一：两个单链中的元素依次分别放入两个栈中，然后依次弾栈找到第一个不相同的元素， 
            最后一个相同的元素就是第一个公共的节点.
    """
    stack_A = []
    stack_B = []
    same_item = []
    while not singlelinklistA.isEmpty():
        stack_A.append(singlelinklistA.pop_head())
    while not singlelinklistB.isEmpty():
        stack_B.append(singlelinklistB.pop_head())
    # print('==================', stack_A)
    # print('========================', stack_B)
    while stack_A and stack_B:
        if stack_A[-1] == stack_B[-1]:
            same_item.append(stack_A.pop())
            stack_B.pop()
    # print('========', same_item)
    return same_item[-1]


def find_common_node2(singlelinklistA, singlelinklistB):
    '''
        思路二:
            判断两个链表哪个长，先让指向长链表的指针向后移动两链表长度差个单位，之后两链表同时移动
            每移动一个单位判断当前的值是否相同，如果值相同则这个值就是第一个公共节点，如果不同则依次向后继续
            查找
    '''
    lenA = singlelinklistA.len()
    lenB = singlelinklistB.len()
    if lenA > lenB:
        k = lenA - lenB
        # print(k)
        while k:
            # print(singlelinklistA.pop_head())
            singlelinklistA.pop_head()
            k -= 1
    else:
        k = lenB - lenA
        # print('else：', k)
        while k:
            singlelinklistB.pop_head()
    while not singlelinklistA.isEmpty() and not singlelinklistB.isEmpty():
        numA = singlelinklistA.pop_head()
        numB = singlelinklistB.pop_head()
        # print(numA, '***********', numB)
        if numA == numB:
            return numA    


def main():
    '''把握住公共节点的最大的特征：公共节点之后的元素都是相同的！！！'''
    singlelinklistA = SingleLinkList()
    singlelinklistB = SingleLinkList()
    # singlelinklistA.insert(1)
    # singlelinklistA.insert(2)
    # singlelinklistA.insert(3)
    # print(singlelinklistA.pop())
    # print(singlelinklistA.pop_head())
    # print(singlelinklistA.pop_head())
    # print(singlelinklistA.pop_head())
    # print(singlelinklistA.pop_head())
    for i in range(0, 11):
        singlelinklistA.append(i)
    for i in range(3, 11):
        singlelinklistB.append(i)
    # print(find_common_node1(singlelinklistA, singlelinklistB))
    print(find_common_node2(singlelinklistA, singlelinklistB))




if __name__ == '__main__':
    main()
