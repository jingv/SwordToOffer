# coding:utf-8
def reorder(item, func):
    if len(item) == 0 or len(item) == 1:
        return item
    print(item)
    begin = 0
    end = len(item) - 1
    while begin < end:
        while not func(item[begin]) and begin < end:
            begin += 1
        while func(item[end]) and begin < end:
            end -= 1
        item[begin], item[end] = item[end], item[begin]
    return item


# 将原先的一个函数解耦为两个函数，使函数具有良好的扩展性，在改变排序条件时仅需要改变函数即可实现相应功能
def is_even(num):
    return (num & 0x1) == 0


if __name__ == '__main__':
    item = [i for i in range(1, 11)]
    print(reorder(item, is_even))
