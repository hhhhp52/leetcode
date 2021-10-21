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
