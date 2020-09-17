def my_regex(regex_input):
    pattern, input_string = regex_input.split('|')
    return pattern == '' or (pattern == '.' and bool(input_string)) or pattern == input_string


if __name__ == '__main__':
    print(my_regex(input()))
