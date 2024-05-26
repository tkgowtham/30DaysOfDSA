class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        temp = nums.copy()
        nums.sort()
        while left < right:
            sums = nums[left] + nums[right]
            if sums == target:
                l = temp.index(nums[left])
                temp[l] = 'done'
                r = temp.index(nums[right])
                temp[r] = 'done'
                return [l, r]
            elif sums < target:
                left += 1
            else:
                right -= 1

        
        return [-1, -1]
