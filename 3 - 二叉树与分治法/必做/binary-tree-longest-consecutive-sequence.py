# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        self.maxLength = 0
        self.dcFind(root)
        return self.maxLength
        
    def dcFind(self, root):
        if not root:
            return {
                        'len': 0,
                        'val': -1
                    }
        
        left = self.dcFind(root.left)
        right = self.dcFind(root.right)
        
        result = {'len': 1,'val':root.val}
        if left['val'] == root.val + 1:
            result['len'] = left['len'] + 1
        if right['val'] == root.val + 1 and result['len'] < right['len'] + 1:
            result['len'] = right['len'] + 1
        if result['len'] > self.maxLength:
            self.maxLength = result['len']
        return result

            