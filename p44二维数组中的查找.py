#coding:utf-8

def seach_num(array, num):
    i = 0
    j = len(array[0]) - 1
    while i < len(array) and j >= 0:
        if array[i][j] == num:
            return True
        elif array[i][j] > num:
            j -= 1
        elif array[i][j] < num:
            i += 1
    return False


def main():
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13],[6, 8, 11, 15]]
    num = eval(input())
    if seach_num(array, num):
        print('存在')
    else:
        print('不存在')


if __name__ == '__main__':
    main()
