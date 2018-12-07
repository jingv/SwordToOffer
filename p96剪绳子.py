# coding:utf-8
def max_num(length):
    # 贪婪算法
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    times_of_3 = length // 3
    if length - times_of_3 * 3 == 1:
        times_of_3 -= 1
    times_of_2 = (length - times_of_3 * 3) / 2
    return 2 ** times_of_2 * 3 ** times_of_3


if __name__ == '__main__':
    print(max_num(10))
