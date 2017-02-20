"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if not root:
            return
        self.traversalHelper(root)

    def traversalHelper(self, root):
        if root.right:
            self.traversalHelper(root.right)
        if root.left:
            self.traversalHelper(root.left)
            leftStart = root.left
            leftEnd = root.left
            while leftEnd.right:
                leftEnd = leftEnd.right
            root.left = None
            rightStart = root.right
            root.right = leftStart
            leftEnd.right = rightStart
        