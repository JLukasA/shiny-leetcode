""" Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array. """
from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)
        for x in count:
            if count[x]>=(len(nums)/2):
                return x