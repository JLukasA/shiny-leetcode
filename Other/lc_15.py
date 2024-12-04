""" Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets. """

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        numsSorted = nums.sort()
        triplets = []
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]:
                continue #skip iteration if current element is duplicate of previous element
            m = l+1
            r = len(nums) - 1
            while m < r:
                val = nums[l] + nums[m] + nums[r]
                if val < 0:
                    m += 1
                elif val > 0:
                    r -= 1
                else:
                    triplets.append([nums[l], nums[m], nums[r]])
                    m +=1
                    while nums[m] == nums[m-1] and m < r:
                        m += 1 #skip iteration if current element is duplicate of previous element
        return triplets