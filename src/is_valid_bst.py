from typing import List
# Alternative strategy, use in-order ordering 
# if the BST is valid, then an in-order traversal will produce 
# a sorted array 
def in_order_traverse(root, result):
    if root is None:
        return 
    in_order_traverse(root.left, result)
    result.append(root.value)
    in_order_traverse(root.right, result)

def is_sorted(elements: List[int]) -> bool:
    # traverse elements two at a time 
    for i in range(1, len(elements)):
        if elements[i] < elements[i-1]:
            return False 
    return True 

# O(n + n) ~ O(2 * n) ~ O(n)
def is_valid_BST(root) -> bool:
    elements = []
    # all traversals are visiting every node in the tree 
    # since we're visiting every node in the tree, O(n)
    in_order_traverse(root, elements)
    print(elements)
    return is_sorted(elements) # O(n)

'''
    10
   /  \
  2   18
      / \
     6  21
'''
bst = TreeNode(10)
bst.left = TreeNode(2)
bst.right = TreeNode(18)
bst.right.left = TreeNode(6)
bst.right.right = TreeNode(21)

print(is_valid_BST(bst))
