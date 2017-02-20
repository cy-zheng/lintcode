"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum2(self, root, target):
        # Write your code here
        self.result = []
        if target is None:
            return self.result
        self.dcHelper(root, target)
        return self.result
        
    def dcHelper(self, root, target):
        dcResult = []
        if not root:
            return dcResult
        temp = self.dcHelper(root.left, target)
        temp.extend(self.dcHelper(root.right, target))
        #dcResult.extend(temp)
        temp.append([])
        for path in temp:
            path.insert(0, root.val)
            if sum(path) == target:
                self.result.append(path[:])
            dcResult.append(path[:])
        return dcResult
            