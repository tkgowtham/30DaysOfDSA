class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if freq[nums[i]] == 0:
                freq[nums[i]] += 1
            else:
                return nums[i]
            
        return 0

'''
Can also use sorting method but it will take O(NlogN) for sorting, so freq array is much more effective.
'''
