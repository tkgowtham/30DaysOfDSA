from sys import maxsize
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        maxi = -maxsize-1

        for i in range(len(nums)):
            sums += nums[i]

            if sums > maxi:
                maxi = sums

            if sums < 0:
                sums = 0

        return maxi
        
