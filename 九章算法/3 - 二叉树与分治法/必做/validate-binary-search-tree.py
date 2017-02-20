"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        result = self.dcHelper(root)
        return result['result']
        
    def dcHelper(self, root):
        if not root:
            return {'result': True, 'min': None, 'max': None}
        else:
            left = self.dcHelper(root.left)
            right = self.dcHelper(root.right)
            if not left['result'] or not right['result']:
                return {'result': False, 'min': None, 'max': None}
            elif (left['max'] and left['max'] >= root.val) \
                or (right['min'] and right['min'] <= root.val):
                return {'result': False, 'min': None, 'max': None}
            else:
                return {
                            'result': True, 
                            'min': left['min'] if left['min'] else root.val, 
                            'max': right['max'] if right['max'] else root.val
                        }