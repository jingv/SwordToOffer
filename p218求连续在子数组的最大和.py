from copy import copy


def find_greatest_sum_of_sub_array(num_li):
    sub_num_li = []
    greatest_sub_num_li = []
    sum_num = 0
    greatest_num = 0
    for i in num_li:
        if sum_num < 0:
            sum_num = i
            sub_num_li = [i]
        else:
            sum_num += i
            sub_num_li.append(i)
            # print(sum_num, '=================', sub_num_li)
        if sum_num > greatest_num:
            # print(sum_num, '============', greatest_num)
            # print(sub_num_li, '******************', greatest_sub_num_li)
            greatest_num = sum_num
            # 浅拷贝与深拷贝问题，默认为浅拷贝，只是拷贝了指向列表的指针
            greatest_sub_num_li = copy(sub_num_li)
    return (greatest_num, greatest_sub_num_li)


if __name__ == '__main__':
    num_li = [1, -2, 3, 10, -4, 7, 2, -5]
    sum_num, sum_num_li = find_greatest_sum_of_sub_array(num_li)
    print(sum_num_li)
    print(sum_num)
