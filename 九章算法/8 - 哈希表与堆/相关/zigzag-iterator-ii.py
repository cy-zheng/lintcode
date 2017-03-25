class ZigzagIterator2:

    # @param {int[][]} a list of 1d vectors
    def __init__(self, vecs):
        # initialize your data structure here
        self.vecs = vecs
        self.lens = [len(v) for v in vecs]
        self.index = [0] * len(vecs)
        self.k = 0

    def next(self):
        # Write your code here
        while self.index[self.k] == self.lens[self.k]:
            self.k += 1
            self.k %= len(self.vecs)
            
        result = self.vecs[self.k][self.index[self.k]]
        self.index[self.k] += 1
        self.k += 1
        self.k %= len(self.vecs)
        return result


    def hasNext(self):
        # Write your code here
        for i in range(len(self.vecs)):
            if self.index[i] < self.lens[i]:
                return True
                
        return False
        

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result