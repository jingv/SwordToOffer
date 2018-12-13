def find_first_not_repeating_char(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return None


if __name__ == "__main__":
    string = 'abaccdeff'
    print(find_first_not_repeating_char(string))
