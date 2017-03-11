"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            size = len(queue)
            dummy = ListNode(0)
            cur = dummy
            for i in range(size):
                treenode = queue.pop(0)
                cur.next = ListNode(treenode.val)
                cur = cur.next
                if treenode.left:
                    queue.append(treenode.left)
                if treenode.right:
                    queue.append(treenode.right)
            result.append(dummy.next)
        return result
                