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
    def maxDepth(self, root):
        # write your code here
        return self.traversalHelper(root, 0)

    def traversalHelper(self, root, depth):
        if not root:
            return depth
        return max(
                    self.traversalHelper(root.left, depth + 1),
                    self.traversalHelper(root.right, depth + 1)
                    )