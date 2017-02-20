"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        self.head = DoublyListNode(0)
        self.tail = self.head
        self.helper(root)
        if self.head.next:
            self.head.next.prev = None
        return self.head.next
        
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        temp = DoublyListNode(root.val)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = self.tail.next
        self.helper(root.right)