# Definition for a multi tree node.
# class MultiTreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         children = [] # children is a list of MultiTreeNode

class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
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
        
        childrenResult = [self.dcFind(c) for c in root.children]
        
        result = {'orderLen': 1,'val':root.val, 'reverseLen': 1}
        
        for cr in childrenResult:
            if cr['val'] == root.val + 1 and result['orderLen'] < cr['orderLen'] + 1:
                result['orderLen'] = cr['orderLen'] + 1
            elif cr['val'] == root.val - 1 and result['reverseLen'] < cr['reverseLen'] + 1:
                result['reverseLen'] = cr['reverseLen'] + 1
        if result['orderLen'] + result['reverseLen'] - 1 > self.maxLength:
            self.maxLength = result['orderLen'] + result['reverseLen'] - 1
        return result