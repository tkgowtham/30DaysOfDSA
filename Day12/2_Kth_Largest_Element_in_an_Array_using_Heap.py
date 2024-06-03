class Heap:
    def __init__(self):
        self._l = []

    def _swap(self, first, second):
        self._l[first], self._l[second] = self._l[second], self._l[first]

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return (index * 2) + 1

    def _right(self, index):
        return (index * 2) + 2

    def insert(self, value):
        self._l.append(value)
        index = len(self._l) - 1
        self._upheap(index)

    def _upheap(self, index):
        if index == 0:
            return
        p = self._parent(index)
        if self._l[index] > self._l[p]: #MaxHeap
            self._swap(index, p)
            self._upheap(p)

    def remove(self):
        if len(self._l) == 0:
            return None
        
        temp = self._l[0]
        last = self._l.pop()
        if len(self._l) != 0:
            self._l[0] = last
            self._downheap(0)

        return temp

    def _downheap(self, index):
        mini = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self._l) and self._l[mini] < self._l[left]: #MaxHeap
            mini = left
        
        if right < len(self._l) and self._l[mini] < self._l[right]: #MaxHeap
            mini = right

        if mini != index:
            self._swap(mini, index)
            self._downheap(mini)

    def getMax(self):
        if not self._l:
            return None
        return self._l[0]

    def heapSort(self):
        sorted_data = []
        while len(self._l) > 0:
            sorted_data.append(self.remove())
        return sorted_data

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = Heap()
        for i in range(len(nums)):
            h.insert(nums[i])

        for i in range(k - 1):
            h.remove()

        return h.getMax()
