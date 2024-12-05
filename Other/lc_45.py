""" You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]. """

class Solution:
    def jump(self, nums: list[int]) -> int:
        left, right, jumps =  0, 0, 0
        goal = len(nums)-1
        while right < goal:
            temp_right = right
            for i in range(left, right+1):
                temp_right = max(temp_right, nums[i]+i)
            left = right + 1
            right = temp_right
            jumps += 1

        return jumps