""" Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead. """

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        SubArrayLen = float('inf')
        l = 0
        r = 0
        CurrentSum = nums[0]
        while r < len(nums):
            # if sum is too small, expand window right side
            if CurrentSum < target:
                r += 1
                if r < len(nums):
                    CurrentSum += nums[r]
            # else, save subarray length and shrink window left side
            else:
                SubArrayLen = min(SubArrayLen, r - l + 1)
                CurrentSum -= nums[l]
                l += 1
        #if no subarray found, return 0
        if SubArrayLen == float('inf'): 
            return 0
        return SubArrayLen 



