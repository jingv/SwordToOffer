#!/usr/bin/env python3
# encoding: utf-8
# @Time    : 2018/12/17 14:04
# @Author  : lalala
# @contact: dllOoOllb.com
# @Site    : 
# @File    : p284反转字符串.py
# @Software: PyCharm


def left_rotate_string(string, k):
    """题目二：左旋转字符串"""
    return string[k:] + string[:k]


def reverse_string(string):
    """题目一：反转单词顺序"""
    # reversed() 与 reverse() 方法都是反转排序
    # reversed(list)    不改变原来list的排序    将副本结果作为返回值返回
    # list.reverse()    改变原来list的排序     没有返回值
    str_li = string.split(' ')
    str_li.reverse()
    # print(str_li)
    # 输出值为None,原因是reverse()方法没有返回值
    # print(str_li.reverse())
    return ' '.join(str_li)


def main():
    s = 'I am a student.'
    # print(reverse_string(s))
    print(left_rotate_string(s, 2))


if __name__ == '__main__':
    main()
