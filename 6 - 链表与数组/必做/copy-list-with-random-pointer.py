# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return
        head = self.copyVal(head)
        head = self.copyRand(head)
        return self.makeCopy(head)
        
    def copyVal(self, head):
        cur = head
        while cur:
            temp = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = temp
            cur = cur.next.next
        return head
        
    def copyRand(self, head):
        cur = head
        while cur: 
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        return head
        
    def makeCopy(self, head):
        dummy = RandomListNode(0)
        cur1 = head
        cur2 = dummy
        while cur1:
            cur2.next = cur1.next
            cur2 = cur2.next
            cur1 = cur1.next.next
        return dummy.next
        