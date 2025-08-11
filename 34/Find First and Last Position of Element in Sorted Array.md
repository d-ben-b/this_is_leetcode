# Find First and Last Position of Element in Sorted Array

## Problem Statement

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with `O(log n)` runtime complexity.

## Approach

As the key word `O(log n)` the method two pointer is wroth to try.
Below is a method I use
to solve this problem:

1. Use two pointers, `left` and `right`, `left` uis equal to index `0` and `right` is equal to the last index of the array i.e. `len(nums) - 1`.
2. the method is to find the index of the first occurrence of the target value and the last occurrence of the target value.
3. By moving `left` when `nums[left] < target` and moving `right` when `nums[right] > target`, we can narrow down the search space.
4. If `nums[left]` and `nums[right]` is equal to `target`, we can update the first occurrence index.
   > [!NOTE]
   > This method is not O(log n) but O(n) in the worst case!

## Better Approach

1. use binSearch instead find `m = (left + right) // 2` and check if `nums[m]` is equal to `target`.
2. If `nums[m]` is equal to `target`, we next have to determind whether we want to find low bound or high bound.
3. so if it is low bond we need to check the index `m - 1` and if it is high bound we need to check the index `m + 1`.
4. We can use a while loop to continue searching until we find the first or last occurrence of the target value.
5. If we find the target value, we can update the first or last occurrence index accordingly.
