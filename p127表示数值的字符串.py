# coding:utf-8
def is_num(str_num):
    try:
        num = eval(str_num)
    except Exception:
        return False
    else:
        return True if type(num) in [float, int] else False


if __name__ == '__main__':
    print(is_num("1+2"))
