"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        result = []
        self.traversalHelper(root, result, [])
        return result
    
    def traversalHelper(self, root, result, path):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            result.append('->'.join(path))
            return
        self.traversalHelper(root.left, result, path[:])
        self.traversalHelper(root.right, result, path[:])