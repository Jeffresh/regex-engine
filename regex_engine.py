def dot_wildcard(pattern, character):
    return pattern == '.' and character != ''


def special_rules(pattern, character):
    return pattern == '' or (character == '' and pattern == '')


def equal_character(pattern, character):
    return pattern == character


def my_regex(pattern_character, character):
    return dot_wildcard(pattern_character, character) \
           or equal_character(pattern_character, character) \
           or special_rules(pattern_character, character)


if __name__ == '__main__':
    character_1, character_2 = input().split("|")
    print(my_regex(character_1, character_2))
