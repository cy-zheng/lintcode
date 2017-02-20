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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        stack = [root]
        while stack:
            now = stack.pop()
            result.append(now.val)
            if now.right:
                stack.append(now.right)
            if now.left:
                stack.append(now.left)
        return result