def get_median(num_li):
    if len(num_li) == 0:
        return None
    elif len(num_li) == 1:
        return num_li[0]
    # 需要保证最大堆中的数据大于最小最中的数据
    # 最小堆, 奇数个数插入最小堆, 保证最小堆中最大的数据小于最大堆中最小的数字
    min_set = []
    # 最大堆, 偶数个数插入最大堆, 保证最大堆中的最小值大于最小堆中的最大值
    max_set = []
    count = 0
    for i in num_li:
        count += 1
        if count & 1:
            # 空列表为False
            if not max_set:
                min_set.append(i)
            elif i > min(max_set):
                min_num_of_max_set = min(max_set)
                max_set.append(i)
                max_set.remove(min_num_of_max_set)
                min_set.append(min_num_of_max_set)
            else:
                min_set.append(i)
        else:
            if not min_set:
                max_set.append(i)
            elif i < max(min_set):
                max_num_of_min_set = max(min_set)
                min_set.append(i)
                min_set.remove(max_num_of_min_set)
                max_set.append(max_num_of_min_set)
            else:
                max_set.append(i)
    # print('max=', max_set)
    # print('min=', min_set)
    if count & 1:
        # print('奇数')
        return max(min_set)
    else:
        # print(max(min_set), ' ', min(max_set))
        return (max(min_set) + min(max_set))/2


if __name__ == "__main__":
    num_li = [i for i in range(1, 100)]
    # print(num_li)
    print(get_median(num_li))
