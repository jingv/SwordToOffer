# coding: utf-8
def print_max_num(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "9"

    s = ''
    s += ("9" + print_max_num(n - 1))

    return s


if __name__ == '__main__':
    print(print_max_num(-1))
