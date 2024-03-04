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

