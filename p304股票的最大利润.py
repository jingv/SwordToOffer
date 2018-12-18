#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p304股票的最大利润.py
@Time    :   2018/12/18 15:00:48
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''


def max_differ(num_li):
    result = 0
    for i in range(1, len(num_li)):
        if result < num_li[i] - min(num_li[:i]):
            result = num_li[i] - min(num_li[:i])
    return result


def main():
    num_li = [9, 11, 8, 5, 7, 12, 16, 14]
    print(max_differ(num_li))


if __name__ == '__main__':
    main()
