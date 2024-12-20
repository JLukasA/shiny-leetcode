""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. """

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    
        nums2 = {}
        for i, c in enumerate(nums):
            target_diff = target - c
            if target_diff in nums2:
                return [i, nums2[target_diff]]
            nums2[c] = i