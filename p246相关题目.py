def del_appear_char(stringA, stringB):
    """从stringA中删除在stringB中出现的字符"""
    for i in stringA:
        if i in stringB:
            stringA = stringA.replace(i, '')
    return stringA


def del_reapting_char(string):
    """删除string中重复的字符"""
    for i in string:
        if string.count(i) > 1 and i not in [' ', ]:
            string = string.replace(i, '')
    return string


def is_anagram(wordA, wordB):
    # anagram(变位词)：两个单词中出现的字母相同，而且每个字母出现的次数也相同，这两个词互为变位词
    for i in wordA:
        if wordB.count(i) != wordA.count(i):
            return False
    return True


if __name__ == '__main__':
    stringA = 'We are students.'
    stringB = 'aeiou'
    # print(del_appear_char(stringA, stringB))
    # print(del_reapting_char(stringA))
    print(is_anagram('live', 'evil'))
