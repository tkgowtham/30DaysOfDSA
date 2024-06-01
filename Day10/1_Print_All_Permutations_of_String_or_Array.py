#TC = O(N!) * (N) SC = O(1)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def findS(s, index):
            if index == len(s):
                result.append(s.copy())

            for i in range(index, len(nums)):
                s[index], s[i] = s[i], s[index]
                findS(s, index + 1)
                s[index], s[i] = s[i], s[index]

        findS(nums, 0)
        return result
