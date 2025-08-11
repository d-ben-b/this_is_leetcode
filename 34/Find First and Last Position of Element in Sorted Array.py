from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1

    # handle edge cases
    if len(nums) == 0:
        return [-1, -1]

    # main method
    while l < r:
        # print(f"{l=} {r=}")
        if nums[l] == target and nums[r] == target:
            return [l, r]
        if nums[l] < target:
            l += 1
        if nums[r] > target:
            r -= 1
    # for some case that number only appears once
    if nums[l] == target:
        return [l, l]
    elif nums[r] == target:
        return [r, r]
    return [-1, -1]


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
