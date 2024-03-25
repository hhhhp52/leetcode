def get_two_sum_dataset():
    data = list()
    set_1 = dict(
        nums=[2, 7, 11, 15],
        target=9,
        result=[0, 1]
    )
    set_2 = dict(
        nums=[3, 2, 4],
        target=6,
        result=[1, 2]
    )
    set_3 = dict(
        nums=[3, 3],
        target=6,
        result=[0, 1]
    )
    data.append(set_1)
    data.append(set_2)
    data.append(set_3)

    return data


def get_add_two_number_dataset():
    data = list()
    set_1 = dict(
        l1=[2, 4, 3],
        l2=[5, 6, 4],
        result=[7, 0, 8]
    )
    set_2 = dict(
        l1=[0],
        l2=[0],
        result=[0]
    )
    set_3 = dict(
        l1=[9, 9, 9, 9, 9, 9, 9],
        l2=[9, 9, 9, 9],
        result=[8, 9, 9, 9, 0, 0, 0, 1]
    )
    data.append(set_1)
    data.append(set_2)
    data.append(set_3)

    return data


def get_longest_substring_without_repeating_characters():
    data = list()
    set_1 = dict(
        s="abcabcbb",
        result=3
    )
    set_2 = dict(
        s="bbbbb",
        result=1
    )
    set_3 = dict(
        s="pwwkew",
        result=3
    )
    data.append(set_1)
    data.append(set_2)
    data.append(set_3)

    return data


def get_string_to_integer_dataset():
    data = list()
    set_1 = dict(
        s="42",
        result=42
    )
    set_2 = dict(
        s="   -42",
        result=-42
    )
    set_3 = dict(
        s="4193 with words",
        result=4193
    )

    set_4 = dict(
        s="words and 987",
        result=0
    )

    set_5 = dict(
        s="-91283472332",
        result=-2147483648
    )

    set_6 = dict(
        s="+-12",
        result=0
    )

    set_7 = dict(
        s="00000-42a1234",
        result=0
    )

    set_8 = dict(
        s="010",
        result=10
    )

    data.append(set_1)
    data.append(set_2)
    data.append(set_3)
    data.append(set_4)
    data.append(set_5)
    data.append(set_6)
    data.append(set_7)
    data.append(set_8)

    return data


def get_roman_to_integer_dataset():
    data = list()
    set_1 = dict(
        s="III",
        result=3
    )
    set_2 = dict(
        s="LVIII",
        result=58
    )
    set_3 = dict(
        s="MCMXCIV",
        result=1994
    )
    data.append(set_1)
    data.append(set_2)
    data.append(set_3)

    return data


def get_longest_common_prefix_dataset():
    data = list()
    set_1 = dict(
        strs=["flower","flow","flight"],
        result="fl"
    )
    set_2 = dict(
        strs=["dog","racecar","car"],
        result=""
    )
   
    data.append(set_1)
    data.append(set_2)

    return data


def get_valid_parentheses_dataset():
    data = list()
    set_1 = dict(
        s="()",
        result=True
    )
    set_2 = dict(
        s="()[]{}",
        result=True
    )
    set_3 = dict(
        s="(]",
        result=False
    )
    set_4 = dict(
        s="([{}])",
        result=True
    )
    set_5 = dict(
        s="(([]){})",
        result=True
    )
    set_6 = dict(
        s="(([])){}",
        result=True
    )
    data.append(set_1)
    data.append(set_2)
    data.append(set_3)
    data.append(set_4)
    data.append(set_5)
    data.append(set_6)

    return data
