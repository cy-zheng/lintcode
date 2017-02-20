"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """ 
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        A_l = []
        B_l = []
        while A:
            A_l.append(A)
            A = A.parent
        while B:
            B_l.append(B)
            B = B.parent
        i = 1
        while i < min(len(A_l), len(B_l)) + 1:
            if A_l[-i] != B_l[-i]:
                return A_l[-(i - 1)]
            i += 1
        return A_l[-(i - 1)]