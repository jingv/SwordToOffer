# coding:utf-8
def combine_array(A, B):
    A.extend(B)
    A.sort(reverse=True)
    return A


if __name__ == '__main__':
    A = [1, 3, 5, 7, 9]
    B = [2, 4, 6, 8, 10]
    print(combine_array(A, B))
