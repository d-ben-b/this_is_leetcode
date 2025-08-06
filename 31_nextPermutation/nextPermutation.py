from typing import List
from math import inf


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pivot = -1
    swap = inf
    swap_index = 0
    n = len(nums)
    # find pivot
    for i in range(1, n):
        if nums[-i] > nums[-i - 1]:
            pivot = n - i - 1
            print(f"pivot is {pivot} value is {nums[pivot]}")
            break
    # the case where pivot is not exist
    if pivot == -1:
        nums.sort()
        return

    # find the number near nums[pivot] but bigger in nums[pivot:]
    for idx in range(pivot, len(nums)):
        if nums[idx] > nums[pivot] and nums[idx] < swap:
            swap = nums[idx]
            swap_index = idx
    print(f"find swap {swap=}")

    # swap
    nums[swap_index], nums[pivot] = nums[pivot], nums[swap_index]
    print(f"nums after swap {nums}")

    # sort nums[pivot + 1:]
    n = len(nums) - pivot - 1
    while n > 1:
        n -= 1
        for i in range(n):
            if nums[pivot + 1 + i] > nums[pivot + 2 + i]:
                print(f"{nums[pivot + 1 + i]=} {nums[pivot + 2 + i]=}")
                nums[pivot + 1 + i], nums[pivot + 2 + i] = (
                    nums[pivot + 2 + i],
                    nums[pivot + 1 + i],
                )


nextPermutation([1, 2, 3])
