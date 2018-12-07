# coding:utf-8
def bubble_sort(item):
    """冒泡排序 正向"""
    for i in range(0, len(item)-1):
        for j in range(i+1, len(item)):
            if item[i] > item[j]:
                item[i], item[j] = item[j], item[i]
    return item


def bubble_sort2(item):
    """冒泡排序 倒序"""
    for i in range(0, len(item)-1):
        for j in range(0, len(item)-i-1):
            if item[j+1] < item[j]:
                item[j+1], item[j] = item[j], item[j+1]
    return item


def select_sort(item):
    """选择排序"""
    for i in range(0, len(item)):
        min_pos = i
        for j in range(i+1, len(item)):
            if item[min_pos] > item[j]:
                min_pos = j
        if min_pos != i:
            item[min_pos], item[i] = item[i], item[min_pos]
    return item


def insert_sort(item):
    """插入排序"""
    for i in range(1, len(item)):
        for j in range(i, 0, -1):
            if item[j] < item[j-1]:
                item[j], item[j-1] = item[j-1], item[j]
            else:
                break
    return item


def quick_sort(item, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_vlue = item[first]
    low = first
    hight = last
    while low < hight:
        while item[hight] > mid_vlue and low < hight:
            hight -= 1
        item[low] = item[hight]
        while item[low] < mid_vlue and low < hight:
            low += 1
        item[hight] = item[low]
    # 结束时 low的值与hight的值相等
    item[low] = mid_vlue
    quick_sort(item, first, low)
    quick_sort(item, low+1, last)
    return item


def shell_sort(item):
    """希尔排序"""
    gaps = [5, 3, 1]
    for gap in gaps:
        for i in range(gap, len(item)):
            j = i
            while j > 0:
                if item[j] < item[j-gap]:
                    item[j], item[j-gap] = item[j-gap], item[j]
                    j -= gap
                else:
                    break
    return item


def meiga_sort(item):
    """归并排序"""
    if len(item) <= 1:
        return item
    mid = len(item) // 2
    left_li = meiga_sort(item[0: mid])
    right_li = meiga_sort(item[mid:])
    left_pos, right_pos = 0, 0
    result = []
    while left_pos < len(left_li) and right_pos < len(right_li):
        if left_li[left_pos] < right_li[right_pos]:
            result.append(left_li[left_pos])
            left_pos += 1
        else:
            result.append(right_li[right_pos])
            right_pos += 1
    # [left:] 与 [right:] 是将左右两部分未添加的部分添加进结果集
    result += (left_li[left_pos:] + right_li[right_pos:])
    return result


def main():
    item = [4, 7, 2, 1, 5, 3, 8, 6]

    print(bubble_sort(item))
    print(bubble_sort2(item))
    print(select_sort(item))
    print(insert_sort(item))
    print(quick_sort(item, 0, len(item)-1))
    print(shell_sort(item))
    print(meiga_sort(item))


if __name__ == '__main__':
    main()
