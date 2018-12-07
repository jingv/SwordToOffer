# coding: utf-8
def num_of_1(num):
    count = 0
    while num:
        num = num & (num - 1)
        count += 1
    return count


if __name__ == '__main__':
    print(num_of_1(-1))
