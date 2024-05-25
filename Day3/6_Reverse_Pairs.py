# O(N^2)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i < j and nums[i] > 2 * nums[j]:
                    count += 1
        return count

