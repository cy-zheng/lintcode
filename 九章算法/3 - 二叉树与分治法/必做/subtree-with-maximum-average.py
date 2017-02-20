"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    def findSubtree2(self, root):
        # Write your code here
        self.maxAvgNode = None
        self.maxAvg = None
        self.dcFind(root)
        return self.maxAvgNode
        
    def dcFind(self, root):
        if not root:
            return {'size': 0, 'sum': 0}
        
        leftSub = self.dcFind(root.left)
        rightSub = self.dcFind(root.right)
        
        result = {
                    'size': leftSub['size'] + rightSub['size'] + 1,
                    'sum': leftSub['sum'] + rightSub['sum'] + root.val
                  }
        if not self.maxAvgNode or self.maxAvg['sum'] * result['size'] \
            < result['sum'] * self.maxAvg['size']:
            self.maxAvgNode = root
            self.maxAvg = result
        return result