def digit_at_index(index):
    if index < 0:
        return -1
    digits = 1
    while True:
        if index > count_of_integers(digits):
            index -= count_of_integers(digits) * digits
            digits += 1
        else:
            break
    # print(index, '=====', digits)
    num, pos_of_num = divmod(index, digits)
    return str(begin_number(digits) + num)[pos_of_num]


def count_of_integers(digits):
    # 返回digits位数的数字一共有多少个
    # 如：digits = 1 返回 10， digits = 2 返回 90
    if digits == 1:
        return 10
    return 9 * 10 ** (digits-1)


def begin_number(digits):
    # 返回digits位数开始的数字
    # 如：digits = 2 返回 10， digits = 3 返回 100
    if digits == 1:
        return 0
    else:
        return 10 ** (digits - 1)


if __name__ == '__main__':
    # print(count_of_integers(1))
    # print(count_of_integers(2))
    # print(count_of_integers(3))
    print(digit_at_index(1001))
