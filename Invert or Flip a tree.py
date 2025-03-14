class Solution(object):
    def invertTree(self, root):
        # Base case: If the node is None, return None (end of recursion)
        if root is None:
            return None
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree
        self.invertTree(root.left)

        # Recursively invert the right subtree
        self.invertTree(root.right)

        # Return the root after inversion
        return root
