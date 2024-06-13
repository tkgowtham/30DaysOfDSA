# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def reverseInorder(self, node, counter, k, kLarge):
        if node == None or counter[0] >= k:
            return

        self.reverseInorder(node.right, counter, k, kLarge)
        counter[0] += 1
        if counter[0] == k:
            kLarge[0] = node.data
            return

        self.reverseInorder(node.left, counter, k, kLarge)
    
    def kthLargest(self,root, k):
        #your code here
        kLarge = [float('inf')]
        counter = [0]

        self.reverseInorder(root, counter, k, kLarge)

        return kLarge[0]
