class Solution(object):
    def isSameTree(self, p, q):
        # Base case: if both nodes are None, the trees are the same (both are empty)
        if not p and not q:
            return True

        # If one node is None and the other is not, the trees are different
        # Or if the values of the nodes are not equal, the trees are different
        if not p or not q or p.val != q.val:
            return False

        # Recursively check the left subtrees and right subtrees
        # Both must be the same for the trees to be considered the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
