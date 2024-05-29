#Brute force approach --> from every index go to left and right find max height O(N^2)
#min(leftmax, rightmax) - hieght[i]

#Better approach : calc the prefix with left max from 0 to n - 1 and suffix with right max from n - 1 to 0
#TC=O(3N) SC = O(2N)
class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        prefix = [height[0]]
        suffix = [height[n-1]]
        for i in range(1,n):
            if height[i] > prefix[i-1]:
                prefix.append(height[i])
            else:
                prefix.append(prefix[i-1])

        for i in range(n-2,-1,-1):
            if height[i] > suffix[0]:
                suffix.insert(0,height[i])
            else:
                suffix.insert(0,suffix[0])

        for i in range(n):
            total += min(prefix[i], suffix[i]) - height[i]

        return total

#Most optimal Approach TC = O(N) SC = O(1)
#use left and right pointers

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)

        left = 0
        right = n - 1

        maxleft = 0
        maxright = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >=  maxleft:
                    maxleft = height[left]
                else:
                    total += maxleft - height[left]

                left += 1

            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    total += maxright - height[right]

                right -= 1

        return total
