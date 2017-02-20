"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        self.maxSum = -99999999
        self.dcSum(root)
        return self.maxSum
        
    def dcSum(self, root, subSum = 0):
        result = subSum
        if not root:
            return
        result += root.val
        if result > self.maxSum:
            self.maxSum = result
        self.dcSum(root.left, result)
        self.dcSum(root.right, result)
        