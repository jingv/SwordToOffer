def longest_substring_without_duplication(string):
    result = ''
    for i in range(0, len(string)):
        sub_string = string[i]
        for j in range(i + 1, len(string)):
            if string[j] not in sub_string:
                sub_string += string[j]
            else:
                break
        if len(result) <= len(sub_string):
            result = sub_string
    print(result)
    return len(result)


if __name__ == '__main__':
    string = 'arabcacfr'
    # string = 'a'
    # string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    # string = 'abcdefg'
    print(longest_substring_without_duplication(string))
