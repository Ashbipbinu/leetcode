# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
       
        # If the main tree (root) is empty, it cannot contain any subtree.
        if not root:
            return False

        # If the current root node matches subRoot, check if the entire tree matches.
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
       
        # If both trees are empty, they are considered identical.
        if not p and not q:
            return True
        
        # If one tree is empty but the other is not, they are not identical.
        if not p or not q:
            return False
        
        # If the values of the current nodes do not match, trees are not identical.
        if p.val != q.val:
            return False

        # Recursively check if both left and right subtrees match.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
