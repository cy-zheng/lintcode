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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.traversalHelper(root)[1]
    
    def traversalHelper(self, root):
        if not root:
            return 0, True
        ldepth, lresult = self.traversalHelper(root.left)
        if lresult:
            rdepth, rresult = self.traversalHelper(root.right)
            if rresult:
                return max(ldepth, rdepth) + 1, abs(ldepth - rdepth) <= 1
            else:
                return max(ldepth, rdepth) + 1, False
        else:
            return ldepth + 1, False