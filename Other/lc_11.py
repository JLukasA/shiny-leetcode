""" You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container. """

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        water = 0
        while l<r:
            curr_water = (r-l) * min(height[l], height[r])
            water = max(water, curr_water)

            if height[l] <= height[r]:
                l += 1
            else: 
                r -= 1
        return water