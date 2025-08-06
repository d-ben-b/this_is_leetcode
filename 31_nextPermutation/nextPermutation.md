# Next Permutation (Problem 31)

## Problem Statement

Implement the `nextPermutation` function, which rearranges numbers into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

## Approach

The algorithm follows these steps:

1. **Find the pivot**: Starting from the right, find the first element that is smaller than its right neighbor. This is our pivot.
2. **Handle the descending case**: If no pivot is found (array is in descending order), reverse the entire array to get the smallest permutation.
3. **Find swap candidate**: Find the smallest element to the right of the pivot that is larger than the pivot.
4. **Swap elements**: Swap the pivot with the identified candidate.
5. **Sort the suffix**: Sort all elements after the pivot position to get the next permutation.

## Complexity Analysis

- **Time Complexity**: O(n) where n is the length of the input array.
- **Space Complexity**: O(1) as we modify the array in-place.

## Code

```python
def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pivot = -1
    swap = inf
    swap_index = 0
    n = len(nums)

    # find pivot - the first element from right that is smaller than its right neighbor
    for i in range(1, n):
        if nums[-i] > nums[-i - 1]:
            pivot = n - i - 1
            break

    # the case where pivot is not found - array is in descending order
    if pivot == -1:
        nums.sort()  # or simply reverse the array
        return

    # find the smallest element in nums[pivot+1:] that is greater than nums[pivot]
    for idx in range(pivot, len(nums)):
        if nums[idx] > nums[pivot] and nums[idx] < swap:
            swap = nums[idx]
            swap_index = idx

    # swap pivot with the found element
    nums[swap_index], nums[pivot] = nums[pivot], nums[swap_index]

    # sort the subarray after pivot (or just reverse it since it's in descending order)
    left = pivot + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

## Examples

1. Input: `nums = [1,2,3]`
   Output: `[1,3,2]`

2. Input: `nums = [3,2,1]`
   Output: `[1,2,3]`

3. Input: `nums = [1,1,5]`
   Output: `[1,5,1]`

## Notes

- The function modifies the array in-place.
- The final sorting of elements after the pivot could be implemented more efficiently by just reversing the subarray (since it's guaranteed to be in descending order after finding the pivot).
