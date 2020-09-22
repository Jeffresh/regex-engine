def dot_wildcard(pattern, character):
    return pattern == '.' and character != ''


def special_rules(pattern, character):
    return pattern == '' or (character == '' and pattern == '')


def equal_character(pattern, character):
    return pattern == character


def process_same_len_strings(pattern, string_):
    if not pattern:
        return True
    elif string_:
        if process_character(pattern[0], string_[0]):
            return process_same_len_strings(pattern[1:], string_[1:])
        else:
            return False
    else:
        return False


def process_character(pattern_character, character):
    return dot_wildcard(pattern_character, character) \
           or equal_character(pattern_character, character) \
           or special_rules(pattern_character, character)


if __name__ == '__main__':
    pattern, string_ = input().split("|")
    print(process_same_len_strings(pattern, string_))
