class LFUCache:

    class Fnode:
        def __init__(self, freq):
            self.freq = freq
            self.pre = self.next = None
            self.child_head = self.child_tail = None
            
    class Knode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.freq = 1
            self.pre = self.next = None
            
    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.length = 0
        self.freq2node = {}
        self.key2node = {}
        self.head = None

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key not in self.key2node:
            if self.length < self.capacity:
                self.length += 1
            else:
                self._popOldKnode()
            knode = self.Knode(key, value)
            self.key2node[key] = knode
            fnode = self._findFnode(knode.freq)
            self._insertKnode(fnode, knode)
        else:
            self._updatePosition(key)
            self.key2node[key].value = value
    
    def _popOldKnode(self):
        knode = self.head.child_head
        del self.key2node[knode.key]
        self.head.child_head = knode.next
        if self.head.child_tail == knode:
            self.head.child_tail = knode.pre
        if self.head.child_head:
            self.head.child_head.pre = None
        if self.head.child_tail:
            self.head.child_tail.next = None
        self._testDeleteFnode(self.head)

    # @return an integer
    def get(self, key):
        # write your code here
        if key in self.key2node:
            self._updatePosition(key)
            return self.key2node[key].value
        return -1
    
    def _updatePosition(self, key):
        # Knode has already existed
        knode = self.key2node[key]
        old_fnode = self.freq2node[knode.freq]
        self._deleteKnode(old_fnode, knode)
        self._testDeleteFnode(old_fnode)
        knode.freq += 1
        new_fnode = self._findFnode(knode.freq)
        self._insertKnode(new_fnode, knode) 
        
    def _insertKnode(self, fnode, knode):    
        if fnode.child_tail:
            fnode.child_tail.next = knode
            fnode.child_tail.next.pre = fnode.child_tail
            fnode.child_tail.next.next = None
            fnode.child_tail = fnode.child_tail.next
        else:
            fnode.child_tail = knode
            fnode.child_tail.next = None
            fnode.child_tail.pre = None
            fnode.child_head = knode

    def _deleteKnode(self, fnode, knode):
        if fnode.child_head == knode:
            fnode.child_head = knode.next
        if fnode.child_tail == knode:
            fnode.child_tail = knode.pre
        if knode.next:
            knode.next.pre = knode.pre
        if knode.pre:
            knode.pre.next = knode.next
            
    def _testDeleteFnode(self, fnode):
        if fnode.child_head is None and fnode.child_tail is None:
            del self.freq2node[fnode.freq]
            if self.head == fnode:
                self.head = fnode.next
            if fnode.pre:
                fnode.pre.next = fnode.next
            if fnode.next:
                fnode.next.pre = fnode.pre
        
    def _findFnode(self, freq):
        if not self.head:
            self.head = self.Fnode(freq)
            self.freq2node[freq] = self.head
            return self.head
        else:
            if freq in self.freq2node:
                return self.freq2node[freq]
            else:
                cur = self.head
                if cur.freq > freq:
                    fnode = self.Fnode(freq)
                    fnode.next = self.head
                    self.head.pre = fnode
                    self.head = fnode
                    self.freq2node[freq] = self.head
                    return self.head
                while cur.next:
                    if cur.freq < freq and cur.next.freq > freq:
                        break
                    cur = cur.next
                tmp = cur.next
                cur.next = self.Fnode(freq)
                cur.next.pre = cur
                cur.next.next = tmp
                if cur.next.next:
                    cur.next.next.pre = cur.next
                self.freq2node[freq] = cur.next
                return cur.next