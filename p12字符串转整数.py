# coding:utf-8
"""
    注意事项：
        特殊字符输入（正负号等）
        最大正整数与最小负整数的溢出
        不能转换为整数的错误处理
"""


def str_int(s):
    num = 0
    s_sign = None
    if s.startswith('-') or s.startswith('+'):
        s_format = s[1:]
        s_sign = s[0]
    else:
        s_format = s
    for i in s_format:
        try:
            num = num*10 + int(i)
        except ValueError as e:
            print('请输入正确的整数字符串')
            return

    if s_sign == '-':
        return 0 - num
    return num


if __name__ == '__main__':
    a = str_int('-234')
    print(a)
