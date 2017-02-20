"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        newCapacity = len(hashTable) * 2
        newHashTable = [None for i in range(newCapacity)]
        for node in hashTable:
            while node:
                hashCode = node.val % newCapacity
                if not newHashTable[hashCode]:
                    newHashTable[hashCode] = ListNode(node.val)
                else:
                    cur = newHashTable[hashCode]
                    while cur.next:
                        cur = cur.next
                    cur.next = ListNode(node.val)
                node = node.next
        return newHashTable
