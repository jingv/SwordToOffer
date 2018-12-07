# coding:utf-8

from timeit import Timer


# 递归方法求第n项斐波拉契数列
def get_fibo1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_fibo1(n-1) + get_fibo1(n-2)


# 循环求解第n项斐波拉契数列
def get_fibo2(n):
    a, b = 1, 1
    i = 0
    while i < n-2:
        a, b = b, a+b
        i += 1
    return b


if __name__ == '__main__':
    # print(get_fibo1(30))
    # print(get_fibo2(30))
    fibo1_timer = Timer('get_fibo1(30)', 'from __main__ import get_fibo1')
    print('get_fibo1: ', fibo1_timer.timeit(1))
    fibo2_timer = Timer('get_fibo2(30)', 'from __main__ import get_fibo2')
    print('get_fibo2: ', fibo2_timer.timeit(1))
