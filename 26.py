from typing import List


def removeDuplicates(nums: List[int]) -> int:
    slow = 0
    fast = 0
    n = len(nums)
    while fast < n:
        if fast < n - 1 and nums[fast] != nums[fast + 1]:
            fast += 1
            slow += 1
            nums[slow] = nums[fast]
        else:
            fast += 1
    return slow + 1 if slow < n else slow


# Example usage
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = removeDuplicates(nums)
    print(f"Result: {result}, Modified List: {nums[:result]}")
