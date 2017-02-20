# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        stack = []
        while root:
            stack.append(root)
            if root.val > p.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                if root.right:
                    root = root.right
                    while root.left:
                        root = root.left
                    return root
                break
        while stack:
            root = stack.pop()
            if root.val > p.val:
                return root
        return None