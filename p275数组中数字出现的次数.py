#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p275数组中数字出现的次数.py
@Time    :   2018/12/17 11:02:09
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''


def find_number_appear_once(num_li):
    """题目一：数组中只出现一次的两个数字"""
    num = 0
    for i in num_li:
        num = num ^ i
    print(num)
    num = return_low1_num(num)
    # num为none说明num=0， 而num说明数组中没有出现奇数次的元素
    if num is None:
        return None

    li1 = []
    li2 = []
    for i in num_li:
        if i & num:
            li1.append(i)
        else:
            li2.append(i)
    print(li1, ' | li2: ', li2)
    single_num1 = 0
    single_num2 = 0
    for i in li1:
        single_num1 = single_num1 ^ i
    for i in li2:
        single_num2 = single_num2 ^ i
    return (single_num1, single_num2)


def return_low1_num(num):
    power_2 = 1
    while power_2 <= num:
        if num & power_2 == power_2:
            return power_2
        power_2 *= 2
    return None


def main():
    num_li = [2, 4, 3, 6, 2, 3, 5, 5]
    # print(return_low1_num(0))
    print('%d %d' % find_number_appear_once(num_li))


if __name__ == '__main__':
    main()
