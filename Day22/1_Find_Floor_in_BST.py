def floorInBST(root, X):

    # Write your Code here.
    def findFloor(root, x):
        if root == None:
            return float('-inf')
        
        if root.data == x:
            return root.data

        if root.data > x:
            return findFloor(root.left, x)

        floor_from_right_subtree = findFloor(root.right, x)

        if floor_from_right_subtree <= x:
            return max(root.data, floor_from_right_subtree)
        else:
            return root.data

    result = findFloor(root, X)
    if result == float('-inf'):
        return None
    return result
