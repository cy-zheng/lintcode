"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        return self.helper(root)
        
    def helper(self, root):
        if not root:
            return 99999999
        if not root.left and not root.right:
            return 1
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        return min(left, right) + 1