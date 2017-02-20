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
    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        self.traverseHelper(root, [], target, result)
        return result
        
    def traverseHelper(self, root, path, target, result):
        if not root:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            if sum(path) == target:
                result.append(path)
        else:
            self.traverseHelper(root.left, path[:], target, result)
            self.traverseHelper(root.right, path[:], target, result)