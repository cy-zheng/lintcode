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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if not root:
            return result
        now = root
        markNode = None
        stack = []
        while stack or now:
            while now:
                stack.append(now)
                now = now.left
            now = stack.pop()
            if not now.right or now.right is markNode:
                result.append(now.val)
                markNode = now
                now = None
            else:
                stack.append(now)
                now = now.right
        return result