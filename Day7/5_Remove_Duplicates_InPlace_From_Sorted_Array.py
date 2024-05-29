#Brute Force Method TC = O(NlogN) + O(N) SC = O(N)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])

        k = len(s)
        j = 0
        s = sorted(list(s))
        for i in s:
            nums[j] = i
            j += 1

        return k

#Optimal Method TC = O(N) SC = O(1), using while loop reduces run time, previous method is more efficent in terms of runtime and space.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
