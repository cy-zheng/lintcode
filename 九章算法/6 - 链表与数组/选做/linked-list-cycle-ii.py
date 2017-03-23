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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head:
            return
        jump1 = jump2 = head
        while True:
            jump1 = jump1.next
            jump2 = jump2.next
            if jump2:
                jump2 = jump2.next
                if not jump2:
                    return
            else:
                return
            if jump1 == jump2:
                break
        
        jump1 = head
        while jump1 != jump2:
            jump1 = jump1.next
            jump2 = jump2.next
            
        return jump1
