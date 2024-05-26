# To solve in O(N) complexity
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = 0
        longest = 1 #min we will have longest 1
        temp = set(nums) #put it in a set, duplicates will be removed, but order not maintained

        for x in temp:
            if (x - 1) not in temp: #we will count in the positive difference only
                count = 1
                i = x
                while (i + 1) in temp: #check if the set contains next number to the number x chosen
                    i += 1
                    count += 1
                longest = max(longest, count)

        return longest
