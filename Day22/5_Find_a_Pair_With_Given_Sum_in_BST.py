# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:
    def __init__(self, root, isReverse):
        self.stack = deque()
        self.reverse = isReverse
        self.pushAll(root)

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        if self.hasNext():
            tempNode = self.stack.pop()
            if not self.reverse:
                self.pushAll(tempNode.right)
            else:
                self.pushAll(tempNode.left)
            return tempNode.val
        return None

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root == None:
            return 
        
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)

        i = l.next()
        j = r.next()

        while i is not None and j is not None and i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = l.next()
            else:
                j = r.next()

        return False
