""" You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array. """

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        hm = {}
        count = 0

        # for each n in nums, check hashmap for target value to make k
        # if found, reduce count of target value by 1 and increase counter
        # if not found, add n to hashmap  
        for n in nums:
            target = k - n
            if target in hm:
                hm[target] -= 1
                count += 1
            
                if hm[target] == 0:
                    del hm[target]
            else:
                hm[n] = hm.get(n, 0) + 1
        return count

            

