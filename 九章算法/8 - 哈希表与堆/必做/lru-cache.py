class LRUCache:
    
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.pre = None
            
    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.cache = {}
        self.nodeMap = {}
        self.queue = ListNode(0)
        self.tail = self.queue
        self.capacity = capacity
        self.length = 0

    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.cache:
            return -1
        # 删除queue中节点
        node = self.nodeMap[key]
        node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        if node == self.tail:
            self.tail = node.pre
        # queue最后插入节点
        self.tail.next = ListNode(key)
        self.tail.next.pre = self.tail
        self.tail = self.tail.next
        self.nodeMap[key] = self.tail
        return self.cache.get(key, -1)
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.nodeMap:
            self.length -= 1
            node = self.nodeMap[key]
            node.pre.next = node.next
            if node.next:
                node.next.pre = node.pre
            if node == self.tail:
                self.tail = node.pre
                self.tail.next = None
        # queue最后插入节点
        self.tail.next = ListNode(key)
        self.tail.next.pre = self.tail
        self.tail = self.tail.next
        self.nodeMap[key] = self.tail
        
        self.cache[key] = value
        self.length += 1 
        if self.length > self.capacity:
            node = self.queue.next
            self.queue.next = self.queue.next.next
            if self.queue.next:
                self.queue.next.pre = self.queue
            del self.cache[node.val]
            del self.nodeMap[node.val]
            self.length -= 1
        
        