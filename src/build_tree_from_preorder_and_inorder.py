"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and outputs a binary tree that adheres to
the ordering of the pre- and in-order traversals.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_helper(root, res):
    if root is None:
        return
    res.append(root.val)
    preorder_helper(root.left, res)
    preorder_helper(root.right, res)

def preorder_traversal(root):
    result = []
    preorder_helper(root, result)
    return result

def inorder_helper(root, res):
    if root is None:
        return
    inorder_helper(root.left, res)
    res.append(root.val)
    inorder_helper(root.right, res)

def inorder_traversal(root):
    result = []
    inorder_helper(root, result)
    return result

from typing import List

def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    # Your code here
    # given preorder and inorder outputs, re-construct the tree that
    # these traversal outputs came from 
    # root will always be the first element in the preorder list 
    # once we know what the root element is, we can find it in the inorder list
    # and see that everything to the left of root in the inorder list comprises
    # the left subtree
    # everything to the right of the root in the inorder list comprises the right subtree
    # identify the elements of the left and right subtrees using the inorder list 
    # then we can find those elements in the preorder list
    # the first element in the preorder list will be the root 

    # 1. find the first element in preorder in the inorder list 
    # 2. split the inorder list around that root 
    # 3. figure out the number of elements in the left and right sides of the inorder 
    # 4. take the same number of elements after the root from the preorder
    # 5. repeat this process by taking the first element in the preorder sublist 
    # as the root
    preorder_index = 0
    
    # make a dict out of the inorder list mapping the elements to their indices 
    inorder_index_map = {val: index for index, val in enumerate(inorder)}

    root, _ = recurse(preorder, preorder_index, inorder_index_map, 0, len(inorder) - 1)

    return root

def recurse(preorder, preorder_index, inorder_index_map, inorder_start, inorder_end):
    # base case(s)
    # when we get through the inorder list, stop recursing 
    if inorder_start > inorder_end:
        return None, preorder_index

    # how are we getting closer to our base case(s)
    root_val = preorder[preorder_index]
    root = TreeNode(root_val)
    preorder_index += 1

    # find the root_val's index in the inorder list 
    root_index = inorder_index_map[root_val]

    # split the inorder list in half 
    # recurse on those halves 
    # left recursive call 
    root.left, preorder_index = recurse(preorder, preorder_index, inorder_index_map, inorder_start, root_index - 1)

    # right recursive call 
    root.right, preorder_index = recurse(preorder, preorder_index, inorder_index_map, root_index + 1, inorder_end)

    return root, preorder_index

preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

tree = build_tree(preorder, inorder)

print(inorder_traversal(tree) == inorder)
print(preorder_traversal(tree) == preorder)
