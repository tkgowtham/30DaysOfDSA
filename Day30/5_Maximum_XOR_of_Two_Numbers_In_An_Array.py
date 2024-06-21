class Node:
    def __init__(self):
        self.links = [None, None]

    def containsKey(self, bit):
        return self.links[bit] is not None

    def get(self, bit):
        return self.links[bit]

    def put(self, bit, node):
        self.links[bit] = node

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit, Node())
            node = node.get(bit)

    def getMax(self, num):
        node = self.root
        max_num = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.containsKey(1 - bit):
                max_num |= (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return max_num
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        maxi = 0
        for num in nums:
            maxi = max(maxi, trie.getMax(num))
        return maxi
