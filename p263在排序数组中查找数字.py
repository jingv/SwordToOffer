#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p263在排序数组中查找数字.py
@Time    :   2018/12/16 14:15:18
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''


def get_missing_number(num_li):
    """题目二：0~n-1中缺失的数字"""
    if len(num_li) <= 0:
        return None
    left = 0
    right = len(num_li) - 1
    while left <= right:
        middle = (right + left) // 2
        if num_li[middle] != middle:
            if middle == 0 or num_li[middle - 1] == middle - 1:
                return middle
            right = middle - 1
        else:
            left = middle + 1
    if left == len(num_li):
        return len(num_li)
    return None


def get_num_same_as_indsex(num_li):
    """题目三：在一个单调递增的数组(每个元素都是整数且唯一)中查找与下标值相同的值"""
    if len(num_li) == 0:
        return None
    left = 0
    right = len(num_li) - 1
    while left < right:
        middle = (left + right) // 2
        if num_li[middle] < middle:
            left = middle + 1
        elif num_li[middle] > middle:
            right = middle - 1
        else:
            return middle
    return None


def main():
    """总结：在对排序数组进行查找操作时使用二分法可以提高效率"""
    # 题目二测试代码
    # num_li = []
    # for i in range(0, 11):
    #     num_li.append(i)
    # num_li.pop(5)
    # print(num_li)
    # print(get_missing_number(num_li))
    # 题目三测试代码
    num_li = [-3, -1, 1, 2, 4, 5]
    print(get_num_same_as_indsex(num_li))


if __name__ == '__main__':
    main()
