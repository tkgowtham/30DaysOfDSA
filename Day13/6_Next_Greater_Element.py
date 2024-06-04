class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        stack = []

        for i in nums2:
            while stack and stack[-1] < i:
                dict1[stack.pop()] = i
            stack.append(i)

        res = []
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                res.append(dict1[nums1[i]])
            else:
                res.append(-1)

        return res
