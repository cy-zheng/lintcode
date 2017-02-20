# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        for item in nestedList[::-1]:
            self.stack.append(item)
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        item = self.stack.pop()
        return item.getInteger()
        
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        if not self.stack:
            return False
        item = self.stack[-1]
        while not item.isInteger():
            self.stack.pop()
            for t in item.getList()[::-1]:
                self.stack.append(t)
            if not self.stack:
                break
            item = self.stack[-1]
        return item.isInteger()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())