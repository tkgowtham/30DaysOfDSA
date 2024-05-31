#Optimal Method
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = []
        for i in range(1,n):
            fact *= i
            nums.append(i)
            
        nums.append(n)

        k -= 1
        ans = ''
        while True:
            ans = ans + str(nums[k // fact])
            nums.pop(k // fact)
            if not nums:
                break
            k = k % fact
            fact = fact // len(nums)

        return ans



#Brute Force (Time Limit Exceeds)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        result = []

        def findS(s, index):
            if index == len(s):
                s = ''
                for i in nums:
                    s += str(i)
                result.append(str(s))
            
            for i in range(index, len(nums)):
                s[index], s[i] = s[i], s[index]
                findS(s, index + 1)
                s[index], s[i] = s[i], s[index]

        findS(nums, 0)
        result.sort()
        return result[k - 1]
