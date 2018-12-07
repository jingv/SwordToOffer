# coding:utf-8
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent < 0:
        return 1 / (power(base, -exponent))

    result = power(base, exponent >> 1)
    result *= result
    if exponent & 0x1 == 1:
        result *= base

    return result


if __name__ == '__main__':
    print(power(4, 0.5))
