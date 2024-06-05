from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        deque_window = deque()
        res = []

        for index, num in enumerate(nums):
            if deque_window and deque_window[0] == index - k:
                deque_window.popleft()

            while deque_window and nums[deque_window[-1]] < num:
                deque_window.pop()

            deque_window.append(index)

            if index >= k - 1:
                res.append(nums[deque_window[0]])

        return res
