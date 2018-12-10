import random


# 解法二
def more_than_half_num(li):
    num = li[0]
    num_count = 1
    for i in li[1:]:
        if num_count == 0:
            num = i
            num_count = 1
        else:
            if i == num:
                num_count += 1
            else:
                num_count -= 1
    return num


if __name__ == '__main__':
    num_li = [2, 2, 2, 2, 1, 1, 2, 3, 3, 3]
    for i in range(100):
        num_li.append(random.randint(0, 10))
    print(more_than_half_num(num_li))
