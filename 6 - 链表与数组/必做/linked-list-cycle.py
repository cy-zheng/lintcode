"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head:
            return False
            
        jump1 = jump2 = head
        while True:
            jump1 = jump1.next
            jump2 = jump2.next
            if jump2:
                jump2 = jump2.next
                if not jump2:
                    return False
            else:
                return False
            if jump1 == jump2:
                break
                
        return True
