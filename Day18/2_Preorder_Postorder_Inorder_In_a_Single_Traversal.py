# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    inorder = []
    preorder = []
    postorder = []

    def traverse(root):
        if root == None:
            return

        preorder.append(root.data)

        traverse(root.left)

        inorder.append(root.data)

        traverse(root.right)

        postorder.append(root.data)

    traverse(root)

    return inorder, preorder, postorder
    pass
