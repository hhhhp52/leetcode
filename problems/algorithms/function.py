from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    ans = list()
    flag = False
    max_range = len(nums)
    for i in range(0, max_range, 1):
        for j in range((i + 1), max_range, 1):
            num_1 = nums[i]
            num_2 = nums[j]
            res = num_1 + num_2
            if res == target:
                ans.append(i)
                ans.append(j)
                flag = True
                break
        if flag:
            break
    return ans


def add_two_number(l1: List[int] = None, l2: List[int] = None) -> List[int]:
    result = list()
    if l1 is not None and l2 is not None:
        l1.reverse()
        l2.reverse()
        l1_num = int("".join(str(e) for e in l1))
        l2_num = int("".join(str(e) for e in l2))
        res_num_str = str(l1_num + l2_num)
        for i in range(0, len(res_num_str), 1):
            result.append(int(res_num_str[i]))
        result.reverse()
    elif l1 is None and l2 is not None:
        result = l2
    elif l1 is not None and l2 is None:
        result = l1

    return result


def longest_substring_without_repeating_characters(s: str) -> int:
    # 用來存儲每個字符在字串中最後一次出現的索引
    char_index = {}

    # 變數用來記錄當前子字串的起始和結束位置
    start = 0
    end = 0

    # 變數用來存儲最長子字串的長度
    max_length = 0

    while end < len(s):
        # 如果當前結束位置的字符不在當前子字串中，則將其添加進去
        if s[end] not in char_index or char_index[s[end]] < start:
            char_index[s[end]] = end
            end += 1
            max_length = max(max_length, end - start)
        else:
            # 如果字符已經在子字串中，則更新起始位置
            start = char_index[s[end]] + 1

    return max_length


def string_to_integer(s: str) -> int:
    result = 0
    # Remove the space
    s_without_start_and_end_space = s.strip(" ")
    # Turn into lower case first
    string_integer_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    string_mark_digits = ["-", "+"]
    mark_string = ""
    start_flag = False
    number_string = ""
    # Start to check number string
    for i in range(0, len(s_without_start_and_end_space), 1):
        if not start_flag:
            # For checking the first alphabet is effective
            if s_without_start_and_end_space[i] not in (string_integer_digits + string_mark_digits):
                break
            else:
                # Effective alphabet, need to check is number or mark
                start_flag = True
                if s_without_start_and_end_space[i] in string_mark_digits:
                    if s_without_start_and_end_space[i] == "-":
                        mark_string = "-"
                    continue
                if s_without_start_and_end_space[i] in string_integer_digits:
                    number_string += s_without_start_and_end_space[i]
        else:
            # After checking the first alphabet, check the next character is number.
            # If not break
            if s_without_start_and_end_space[i] not in string_integer_digits:
                break
            else:
                number_string += s_without_start_and_end_space[i]

    start = 0
    # Check NumberString
    if number_string:
        # If Start by 0, we should dismiss 0, ex "010" => "10"
        for i in range(0, len(number_string), 1):
            if number_string[i] != "0":
                break
            else:
                start += 1

        if start < len(number_string):
            result = int(mark_string+number_string[start:])

    # Result only accept between [-2^31, 2^31-1]
    if result < -2**31:
        result = -2**31
    elif result > 2**31-1:
        result = 2**31-1

    return result


def roman_to_integer(s: str) -> int:
    roman_list = ["I", "V", "X", "L", "C", "D", "M"]

    roman_number = dict(
        I=1,
        V=5,
        X=10,
        L=50,
        C=100,
        D=500,
        M=1000
    )

    result = 0
    start_index = 0
    max_index = len(s) - 1
    while True:
        if start_index == max_index:
            result += roman_number[s[start_index]]
            break
        elif start_index < max_index:
            if roman_list.index(s[start_index]) >= roman_list.index(s[start_index + 1]):
                result += roman_number[s[start_index]]
                start_index = start_index + 1
                if start_index == max_index:
                    result += roman_number[s[start_index]]
                    break
            else:
                result = result - roman_number[s[start_index]] + roman_number[s[start_index + 1]]
                start_index = start_index + 2
                if start_index > max_index - 1:
                    if start_index == max_index:
                        result += roman_number[s[start_index]]
                    break

    return result
