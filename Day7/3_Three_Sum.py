class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if i != 0 and nums[i] == nums[i-1]: #Skip Duplicates
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums < 0:
                    j += 1
                elif sums > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: #Skip Duplicates
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
