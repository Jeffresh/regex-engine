def my_regex(pattern, input_string):
    return pattern == '' \
           or (pattern == '.' and bool(input_string)) \
           or (pattern == input_string)


def regex_engine(raw_input):
    split_pattern = '|'
    pattern, input_string = raw_input.split(split_pattern)
    wildcard = None
    if len(pattern) > 0:
        wildcard = '^' if pattern[0] == '^' else None
        pattern = pattern[1:] if wildcard else pattern
    if engine(pattern, input_string):
        return True
    elif input_string and not wildcard:
        return regex_engine(pattern + '|' + input_string[1:])
    else:
        return False


def engine(pattern, input_string):
    if not pattern:
        return True
    elif not input_string and pattern == '$':
        return True
    elif not input_string:
        return False
    else:
        if my_regex(pattern[0], input_string[0]):
            return engine(pattern[1:], input_string[1:])
        elif pattern[0] == '?':
            return engine(pattern[1:], input_string)
        elif pattern[0] == '*' and (len(input_string)) == 1:
            return engine(pattern[1:], input_string)
        elif (pattern[0] == '*' or pattern[0] == '+') and (
                len(input_string) > 1 and input_string[0] == input_string[1]):
            return engine(pattern, input_string[2:])
        elif len(pattern) > 1 and (pattern[1] == '?' or pattern[1] == '*' or pattern[0] == '+'):
            return engine(pattern[2:], input_string)
        else:
            return False


if __name__ == '__main__':
    print(regex_engine(input()))
