# coding:utf-8
def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        while n-2:
            a, b = b, a+b
            n -= 1
        return b


for i in [3, 5, 10, 0, 1, 2, 40, 50, 100]:
    print(fibo(i))
