""" You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise. """

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # goal is reaching end of list
        goal = len(nums)-1
        #starting from the second last index, iterating backwards
        for i in range(goal -1, -1, -1):
            #if you can reach the goal from current index
            if i + nums[i] >= goal:
                #move the goal to current index, which can reach last index
                goal = i

        #return true if last index can be reached from first index
        return goal == 0
