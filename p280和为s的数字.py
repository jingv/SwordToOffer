#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   p280和为s的数字.py
@Time    :   2018/12/17 13:29:54
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
"""


def find_numbers_with_sum(num_li, k):
    """题目一：和为s的两个数字
    输入一个递增排序的数组和一个数字s，在数组中查找两个数，使他们的和正好是s，
    如果有多对数字的和等于s，输出任意一对即可
    """
    left = 0
    right = len(num_li) - 1
    while left < right:
        if num_li[left] + num_li[right] < k:
            left += 1 
        elif num_li[left] + num_li[right] > k:
            right -= 1
        else:
            return num_li[left], num_li[right]
    return


def find_continuous_sequence(k):
    """题目二：和为s的连续正数序列"""
    """输入一个正数s，打印出所有和为s的正数序列（至少含有两个数）"""
    result = []
    left = 1
    right = 2
    while left < k:
        sum_nums = sum([i for i in range(left, right + 1)])
        if sum_nums > k:
            left += 1
        elif sum_nums < k:
            right += 1
        else:
            result.append([i for i in range(left, right + 1)])
            # 如果当前和为k，right向前走一步，或者left向前走一步
            left += 1
    return result


def main():
    # 题目一测试
    # num_li = [1, 2, 4, 7, 11, 15]
    # k = eval(input('输入k的值: '))
    # print(find_numbers_with_sum(num_li, k))

    # 题目二测试
    print(find_continuous_sequence(15))


if __name__ == '__main__':
    main()
