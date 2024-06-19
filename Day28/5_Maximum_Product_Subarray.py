class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 1
        ans = float('-inf')
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            ans = max(ans, max(prefix, suffix))


        return ans
