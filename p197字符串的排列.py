def core(s, begin=0):
    '''
        s为要进行排序的字符串的列表形式
        begin为排序开始的位置
    '''
    if begin == len(s):
        print(''.join(s))
    else:
        for i in range(begin, len(s)):
            s[i], s[begin] = s[begin], s[i]
            next_begin = begin + 1
            core(s, next_begin)
            s[i], s[begin] = s[begin], s[i]


def permutation(s):
    """permutation 变换、变动、排列"""
    """初始化字符串列表， 调用核心算法"""
    if len(s) == 0:
        return None
    s_li = [i for i in s]
    core(s_li)


if __name__ == '__main__':
    s = 'abcdefgh'
    permutation(s)
