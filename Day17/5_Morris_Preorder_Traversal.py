'''
	 
	 Following is the Binary Tree node structure:
	 
	 class TreeNode:
	     def __init__(self, data=0, left=None, right=None):
	         self.data = data
	         self.left = left
	         self.right = right
'''

def getPreOrderTraversal(root):
    ans = []

    def traverse(root, ans):
        while root:
            if root.left is None:
                ans.append(root.data)
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right

                if prev.right is None:
                    prev.right = root
                    ans.append(root.data)
                    root = root.left
                else:
                    prev.right = None
                    root = root.right

        return ans

    ans = traverse(root, ans)
    return ans
