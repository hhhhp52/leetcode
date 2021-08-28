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
