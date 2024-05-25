#O(NlogN) --> Hashing based algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] += 1
        
        ans = []
        for i in dict1:
            if dict1[i] > len(nums) / 3:
                ans.append(i)
        
        return ans

#O(N) --> Extended Booyer Moore's Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        element1 = None
        element2 = None
        for i in range(len(nums)):
            if count1 == 0 and nums[i] != element2:
                element1 = nums[i]
                count1 = 1
            elif count2 == 0 and nums[i] != element1:
                element2 = nums[i]
                count2 = 1
            elif element1 == nums[i]:
                count1 += 1
            elif element2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        ans = []

        temp_count1 = 0
        temp_count2 = 0
        for i in range(len(nums)):
            if element1 == nums[i]:
                temp_count1 += 1
            elif element2 == nums[i]:
                temp_count2 += 1
        
        if temp_count1 > len(nums) // 3:
            ans.append(element1)
        
        if temp_count2 > len(nums) // 3:
            ans.append(element2)

        return ans
