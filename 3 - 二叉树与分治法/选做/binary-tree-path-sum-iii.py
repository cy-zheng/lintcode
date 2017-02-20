"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    # @param {ParentTreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum3(self, root, target):
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
        left = self.dcHelper(root.left, target)
        right = self.dcHelper(root.right, target)
        for l in left:
            for r in right:
                if sum(l) + root.val + sum(r) == target:
                    temp = l[::-1]
                    temp.append(root.val)
                    temp.extend(r[:])
                    self.result.append(temp)
                    self.result.append(temp[::-1])
        temp = left[:]
        temp.extend(right[:])
        temp.append([])
        for path in temp:
            path.insert(0, root.val)
            if sum(path) == target:
                self.result.append(path[:])
                if len(path) > 1:
                    self.result.append(path[::-1])
            dcResult.append(path[:])
        return dcResult

        