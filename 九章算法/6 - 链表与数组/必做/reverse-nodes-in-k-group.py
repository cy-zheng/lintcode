# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        if not head or not k:
            return head
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        cur = pre = dummy
        while cur.next:
            cur = cur.next
            count += 1
            if count % k == 0:
                pre.next = self.reverse(pre.next, k)
                count = 0
                for i in range(k):
                    pre = pre.next
                cur = pre
        return dummy.next
        
    def reverse(self, head, k):
        pre = head
        cur = head.next
        count = 1
        while count < k:
            count += 1
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head.next = cur
        return pre