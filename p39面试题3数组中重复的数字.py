# coding: utf-8
"""
    注意处理：空指针数组以及边界条件
"""
from timeit import Timer


def method_for_same1(array):
    if len(array) == 0:
        return None
    array.sort()
    for i in range(0, len(array)-1):
        if array[i] == array[i+1]:
            return array[i]
    return None


def method_for_same2(array):
    single_asrry = []
    if len(array) == 0:
        return None
    for i in array:
        if i in single_asrry:
            return i
        else:
            single_asrry.append(i)
    return None


def method_for_same3(array):
    if len(array) == 0:
        return None
    for i in range(0, len(array)):
        while i != array[i]:
            if array[i] == array[array[i]]:
                return array[i]
            a = array[i]
            b = array[array[i]]
            array[i], array[a] = array[a], array[i]
    return None


if __name__ == '__main__':
    array = [2, 3, 1, 0, 2, 5, 3]

    # print(method_for_same1(array))

    # print(method_for_same2(array))

    # print(method_for_same3(array))

    timer1 = Timer('method_for_same1([2, 3, 1, 0, 2, 5, 3])', 'from __main__ import method_for_same1')
    timer2 = Timer('method_for_same2([2, 3, 1, 0, 2, 5, 3])', 'from __main__ import method_for_same2')
    timer3 = Timer('method_for_same3([2, 3, 1, 0, 2, 5, 3])', 'from __main__ import method_for_same3')

    print('method_for_same1: ', timer1.timeit(100))
    print('method_for_same2: ', timer2.timeit(100))
    print('method_for_same3: ', timer3.timeit(100))

