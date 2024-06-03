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
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        h = Heap()
        result = []
        
        # Use a set to keep track of visited indices
        visited = set()
        
        # Initialize the heap with the largest elements combination
        h.insert((A[0] + B[0], 0, 0))
        visited.add((0, 0))
        
        for _ in range(C):
            if not h._l:
                break
            
            current_sum, i, j = h.remove()
            result.append(current_sum)
            
            # Next element in A
            if i + 1 < len(A) and (i + 1, j) not in visited:
                h.insert((A[i + 1] + B[j], i + 1, j))
                visited.add((i + 1, j))
            
            # Next element in B
            if j + 1 < len(B) and (i, j + 1) not in visited:
                h.insert((A[i] + B[j + 1], i, j + 1))
                visited.add((i, j + 1))
        
        return result
