# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left  # Move left
        elif p.val > root.val and q.val > root.val:
            root = root.right  # Move right
        else:
            return root  # Found LCA
    return None
