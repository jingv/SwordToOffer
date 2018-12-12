def for_assist_array(array_origan):
    rows = len(array_origan)
    cols = len(array_origan[0])

    if rows == 0 or cols == 0:
        return None
    assist_array = []
    # 初始化第一行
    num = []
    for i in array_origan[0]:
        if len(num) == 0:
            num.append(i)
        else:
            num.append(i + num[-1])
    assist_array.append(num)
    # 初始化第一列
    num = assist_array[0][0]
    for i in array_origan[1:]:
        num += i[0]
        assist_array.append([num])

    for row in range(1, rows):
        for col in range(1, cols):
            if assist_array[row-1][col] > assist_array[row][col-1]:
                assist_array[row].append(assist_array[row-1][col] +
                                         array_origan[row][col])
            else:
                assist_array[row].append(assist_array[row][col-1] +
                                         array_origan[row][col])
    return assist_array[rows - 1][cols - 1]


if __name__ == '__main__':
    # array = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    array = [[1]]
    print(for_assist_array(array))
