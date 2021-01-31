import math
from typing import List


class BinarySearch:
    def serch(self, nums: List[int], target: int) -> int:
        minn = 0
        maxx = len(nums) - 1
        while minn <= maxx:
            index = math.floor((minn + maxx) / 2)
            if nums[index] == target:
                return index
            elif nums[index] < target:
                minn = index + 1
            else:
                maxx = index - 1
        return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    nums = sorted(nums)
    print(len(nums))

    for i in range(12):
        j = BinarySearch().serch(nums, i + 1)
        print(j)
