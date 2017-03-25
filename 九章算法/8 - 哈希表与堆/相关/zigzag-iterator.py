class ZigzagIterator:

    # @param {int[]} v1 v2 two 1d vectors
    def __init__(self, v1, v2):
        # initialize your data structure here
        self.v1 = v1
        self.v2 = v2
        self.v1_index = 0
        self.v2_index = 0
        self.flag = True

    def next(self):
        # Write your code here
        if self.v1_index < len(self.v1) and self.v2_index < len(self.v2):
            if self.flag:
                result = self.v1[self.v1_index]
                self.v1_index += 1
            else:
                result = self.v2[self.v2_index]
                self.v2_index += 1
            self.flag = not self.flag
            return result
        if self.v1_index < len(self.v1):
            result = self.v1[self.v1_index]
            self.v1_index += 1
            return result
        if self.v2_index < len(self.v2):
            result = self.v2[self.v2_index]
            self.v2_index += 1
            return result

    def hasNext(self):
        # Write your code here
        return self.v1_index < len(self.v1) or self.v2_index < len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result