from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1
    if len(nums) == 0:
        return [-1, -1]
    low = binSearch(nums, target, low=True)
    if low == -1:
        return [low, low]
    right = binSearch(nums, target, low=False)
    return [low, right]


def binSearch(arr, tar, low) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == tar:
            if low:
                if l == m or arr[m - 1] < tar:
                    return m
                else:
                    r = m - 1
            else:
                if r == m or arr[m + 1] > tar:
                    return m
                else:
                    l = m + 1
        elif arr[m] > tar:
            r = m - 1
        else:
            l = m + 1
    return -1


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
