#Brute Force
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def findS(arr, ind, n, ss):
            if ind == n:
                ss.sort()
                if ss not in result:
                    result.append(ss)
                return

            findS(arr, ind + 1, n, ss + [arr[ind]])
            findS(arr, ind + 1, n, ss)

        n = len(nums)
        findS(nums, 0, n, [])

        return result

# O(2^n * k) for both TC and SC, k is the average length of subsets. Previous method is much better
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        
        def findS(nums, index, n):
            result.append(subset.copy())
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                findS(nums, i + 1, n)
                subset.pop()
        
        findS(nums, 0, len(nums))
        return result
