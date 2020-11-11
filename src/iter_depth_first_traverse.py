# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# pre-order depth-first traversal 
def iter_depth_first_traverse(root):
    if root is None:
        return []

    result = []
    stack = []
    stack.append(root)

    while len(stack) != 0:
        node = stack.pop()

        if node.right is not None:
            stack.append(node.right)

        result.append(node.val)

        if node.left is not None:
            stack.append(node.left)

    return result 
	