#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   p300圆圈中最后的数字.py
@Time    :   2018/12/18 14:41:56
@Author  :   Jeyson
@Version :   1.0
@Contact :   dllOoOllb@163.com
@Desc    :   None
'''


def the_last_num(num_li, m):
    """删除第m个数字"""
    # 当前是第index个数字
    index = 0
    num_pos = m
    while num_li:
        if num_pos == 1:
            print(num_li.pop(index))
            num_pos = m
        else:
            num_pos -= 1
            index += 1
        
        if index == len(num_li):
            index = 0


def main():
    num_li = [0, 1, 2, 3, 4]
    the_last_num(num_li, 6)
    # print(num_li)


if __name__ == '__main__':
    main()
