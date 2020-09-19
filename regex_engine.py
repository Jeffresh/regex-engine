def my_regex(pattern, input_string):
    return pattern == '' or (pattern == '.' and bool(input_string)) or pattern == input_string


def regex_engine(raw_input):
    split_pattern = '|'
    pattern, input_string = raw_input.split(split_pattern)
    if engine(pattern, input_string):
        return True
    elif input_string:
        return regex_engine(pattern + '|' + input_string[1:])
    else:
        return False


def engine(pattern, input_string):
    if not pattern:
        return True
    elif not input_string:
        return False
    else:
        if my_regex(pattern[0], input_string[0]):
            return engine(pattern[1:], input_string[1:])
        else:
            return False


if __name__ == '__main__':
    print(regex_engine(input()))
