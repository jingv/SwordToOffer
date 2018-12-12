def min_num_of_array(num_li):
    if len(num_li) == 0:
        return None
    elif len(num_li) == 1:
        return num_li[0]
    else:
        num_li.sort()
        min_num = num_li[0]
        for i in num_li[1:]:
            num1 = int(str(min_num) + str(i))
            num2 = int(str(i) + str(min_num))
            if num1 > num2:
                min_num = num2
            else:
                min_num = num1
        return min_num


if __name__ == '__main__':
    # num_li = [3, 32, 321]
    # num_li = [3, 321]
    num_li = [321]
    print(min_num_of_array(num_li))
