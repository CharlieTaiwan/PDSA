from typing import List
from operator import itemgetter
import math


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = sorted(enumerate(nums), key=itemgetter(1))
        num = [value for index, value in num_list]
        list_len = len(num)

        for i in range(list_len):
            minn = i + 1
            maxx = list_len - 1
            relative = target - num[i]
            while minn <= maxx:
                index = math.floor((minn + maxx) / 2)
                if i == index:
                    continue
                elif num[index] == relative:
                    return [num_list[i][0], num_list[index][0]]
                elif num[index] < relative:
                    minn = index + 1
                else:
                    maxx = index - 1
        return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 7
    print(Solution().twoSum(nums, target))
