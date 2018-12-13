def is_ugly_num(num):
    while(num % 2 == 0):
        num /= 2
    while(num % 2 == 0):
        num /= 2
    while(num % 2 == 0):
        num /= 2
    return True if num == 1 else False


def finduglynum2():
    uglynum = [1]
    n = int(input())
    # 记录当前是第i个数
    i = 1
    t2 = min_ugly2 = 0
    t3 = min_ugly3 = 0
    t5 = min_ugly5 = 0
    while i < n:
        # 列表值外最小的丑数并将其加入列表
        for x in range(t2, len(uglynum)):
            min_ugly2 = uglynum[x]*2
            # print("m2:",m2,end=" ")
            if min_ugly2 > uglynum[-1]:
                t2 = x
                # print("t2:",t2)
                break
        for x in range(t3, len(uglynum)):
            min_ugly3 = uglynum[x]*3
            # print("m3:",m3,end=" ")
            if min_ugly3 > uglynum[-1]:
                t3 = x
                # print("t3:",t3)
                break
        for x in range(t5, len(uglynum)):
            min_ugly5 = uglynum[x]*5
            # print("m5",m5,end=" ")
            if min_ugly5 > uglynum[-1]:
                t5 = x
                # print("t5:",t5)
                break
        uglynum.append(min(min_ugly2, min_ugly3, min_ugly5))
        i += 1
    print(uglynum)


if __name__ == '__main__':
    # 测试
    finduglynum2()
