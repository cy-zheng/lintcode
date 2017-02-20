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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        stack = []
        now = root
        while now or stack:
            while now:
                stack.append(now)
                now = now.left
            now = stack.pop()
            result.append(now.val)
            now = now.right
        return result