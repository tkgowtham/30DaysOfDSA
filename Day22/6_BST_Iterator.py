# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.pushAll(root)

    def next(self) -> int:
        if self.hasNext():
            tempNode = self.stack.pop()
            self.pushAll(tempNode.right)
            return tempNode.val
        return -1

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
