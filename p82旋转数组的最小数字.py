# coding:utf-8
def seach_min(item):
    if len(item) <= 1:
        return item
    first = 0
    last = len(item)-1
    while item[first] >= item[last]:
        if last - first == 1:
            mid = last
            break
        mid = (first + last) // 2
        if item[first] == item[last] == item[mid]:
            # min_num = item[0]
            # for i in range(1, len(item)):
            #     if min_num > item[i]:
            #         min_num = item[i]
            # return min_num
            return min(item)
        elif item[mid] > item[first]:
            first = mid
        elif item[mid] < item[last]:
            last = mid
    return item[mid]


if __name__ == '__main__':
     # item = [3, 4, 5, 1, 2]
     item = [1, 1, 1, 0, 1]
     print(seach_min(item))



