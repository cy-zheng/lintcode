"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    def findSubtree(self, root):
        # Write your code here
        self.minSum = None
        self.minSumNode = None
        self.dcFind(root)
        return self.minSumNode
    
    def dcFind(self, root):
        if not root:
            return 0
        
        result = self.dcFind(root.left) + self.dcFind(root.right) + root.val
        
        if not self.minSumNode or self.minSum > result:
            self.minSum = result
            self.minSumNode = root
        
        return result