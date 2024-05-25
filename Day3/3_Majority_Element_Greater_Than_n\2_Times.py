class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0
        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count = 1
            elif element == nums[i]:
                count += 1
            else:
                count -= 1

        count_confirm = 0
        for i in range(len(nums)):
            if element == nums[i]:
                count_confirm += 1

        if count_confirm > len(nums)/2:
            return element
        else:
            return -1
