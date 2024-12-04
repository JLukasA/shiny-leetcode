""" Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array. """

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers l, r
        # starting  
        l = 0
        for r in range(len(nums)): #looking through all positions
            if nums[r] != 0: #if non-zero value found on right pointer
                nums[r], nums[l] = nums[l], nums[r] # swap positions of values
                l += 1 # and take a step with left pointer



