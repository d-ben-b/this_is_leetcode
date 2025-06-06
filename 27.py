def removeElement(nums: List[int], val: int) -> int:
    slow = 0
    fast = 0
    n = len(nums)
    while fast < n:
        if nums[fast] == val:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    return slow
