# 未解决
# 未解决
# 未解决
# 未解决
# 未解决
# 未解决
# 未解决
# 未解决


def number_of_1between1_and_n(num):
    if num < 0:
        return 0
    elif num < 9:
        return 1
    else:
        num = str(num)
        if int(num[0]) > 1:
            return 10 ** (len(num) - 1) + number_of_1between1_and_n(int(num[1:]))
        elif int(num[0]) == 1:
            return int(num[1:]) + 1 + number_of_1between1_and_n(int(num[1:]))


if __name__ == '__main__':
    while True:
        n = input()
        if not n:
            break
        n = eval(n)
        print(number_of_1between1_and_n(n))
