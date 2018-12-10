import random


def get_last_numbers(num_li, k):
    result_li = []
    for i in num_li:
        if len(result_li) < k:
            result_li.append(i)
        else:
            if max(result_li) > i:
                result_li.remove(max(result_li))
                result_li.append(i)
    return result_li


if __name__ == '__main__':
    num_li = []
    k = 4
    for i in range(100):
        num_li.append(random.randint(0, 100))
    print(get_last_numbers(num_li, k))
