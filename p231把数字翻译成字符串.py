def get_translation_count_recursion(num=-1):
    # print(num)
    if len(str(num)) == 0:
        return 0
    if len(str(num)) == 1:
        return 1
    # if len(str(num)) == 2:
    #     return 2 if 10 <= num <= 25 else 1
    if 10 <= int(str(num)[:2]) <= 25:
        # print(int(str(num)[:2]))
        return get_translation_count_recursion(int(str(num)[1:])) + \
            get_translation_count_recursion(int(str(num)[2:]))
    else:
        return get_translation_count_recursion(int(str(num)[1:]))


def get_translation_count_cyle(num):
    # count = 0
    # queue = [num]
    pass


if __name__ == '__main__':
    num = 12258
    print(get_translation_count_recursion(num))
