# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive2(self, root):
        # Write your code here
        self.maxLength = 0
        self.dcFind(root)
        return self.maxLength
        
    def dcFind(self, root):
        if not root:
            return {
                        'orderLen': 0,
                        'val': -1,
                        'reverseLen': 0,
                    }
        
        left = self.dcFind(root.left)
        right = self.dcFind(root.right)
        
        result = {'orderLen': 1,'val':root.val, 'reverseLen': 1}
        if left['val'] == root.val + 1:
            result['orderLen'] = left['orderLen'] + 1
        if right['val'] == root.val + 1 and result['orderLen'] < right['orderLen'] + 1:
            result['orderLen'] = right['orderLen'] + 1
        if left['val'] == root.val - 1:
            result['reverseLen'] = left['reverseLen'] + 1
        if right['val'] == root.val - 1 and result['reverseLen'] < right['reverseLen'] + 1:
            result['reverseLen'] = right['reverseLen'] + 1
        if result['orderLen'] + result['reverseLen'] - 1 > self.maxLength:
            self.maxLength = result['orderLen'] + result['reverseLen'] - 1
        return result