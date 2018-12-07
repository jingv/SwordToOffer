# coding:utf-8

"""
    求链表中倒数第k个节点
    注意事项
        总结点小于k的情况
        输入的k值为0
        传入空指针
"""
link = list(range(1, 11))
# 用户输入k值
k = eval(input("请输入k的值： "))
link_len = len(link)
if k == 0 or k > link_len:
    print('您输入的k值有误')
else:
    i = k - 1
    j = 0
    while i < link_len-1:
        i += 1
        j += 1
    print(link[j])
