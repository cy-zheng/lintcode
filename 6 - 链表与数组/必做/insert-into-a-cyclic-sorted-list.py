"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param {ListNode} node a list node in the list
    # @param {int} x an integer
    # @return {ListNode} the inserted new list node
    def insert(self, node, x):
        # Write your code here
        inserted = ListNode(x)
        #自己也要满足cyclic
        inserted.next = inserted
        if not node:
            return inserted
            
        head = node
        node = node.next
        while True:
            if (node.val <= x and node.next.val < node.val) or \
                (node.val < x and x <= node.next.val) or \
                (node.next.val >= x and node.next.val < node.val) or \
                head == node:
                break
            node = node.next
                
        temp = node.next
        node.next = inserted
        node.next.next = temp
        return node.next