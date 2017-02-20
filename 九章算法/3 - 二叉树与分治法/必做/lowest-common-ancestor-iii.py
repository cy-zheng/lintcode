"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        result = self.dcHelper(root, A, B)
        return result['result']

    def dcHelper(self, root, A, B):
        if not root:
            return {
                        'foundA': False,
                        'foundB': False,
                        'result': None
                    }
        else:
            left = self.dcHelper(root.left, A, B)
            right = self.dcHelper(root.right, A, B)
            result = {
                            'foundA': left['foundA'] or right['foundA'],
                            'foundB': left['foundB'] or right['foundB'],
                            'result': left['result'] if left['result'] else right['result']
                      }
            if root == A:
                result['foundA'] = True
            if root == B:
                result['foundB'] = True
            if result['result'] is None and result['foundA'] and result['foundB']:
                result['result'] = root
            return result