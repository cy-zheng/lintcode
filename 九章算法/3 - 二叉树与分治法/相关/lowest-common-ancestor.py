"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        pathA = self.traversalHelper(root, [], A)
        pathB = self.traversalHelper(root, [], B)
        if not pathA or not pathB or not root:
            return
        temp = None
        for i in range(min(len(pathA), len(pathB))):
            if pathA[i] == pathB[i]:
                temp = pathA[i]
            else:
                break
        return temp

    def traversalHelper(self, root, path, value):
        if not root:
            return
        path.append(root)
        if root is value:
            return path
        pathLeft = self.traversalHelper(root.left, path[:], value)
        pathRight = self.traversalHelper(root.right, path[:], value)
        return pathLeft if pathLeft else pathRight
