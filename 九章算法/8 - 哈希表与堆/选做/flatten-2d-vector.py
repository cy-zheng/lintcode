class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec = vec2d
        self.index = 0
        self.index2d = 0
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        if isinstance(self.vec[self.index], list):
            result = self.vec[self.index][self.index2d]
            self.index2d += 1
        else:
            result = self.vec[self.index]
            self.index += 1
        return result
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.index < len(self.vec):
            if isinstance(self.vec[self.index], list):
                if self.index2d < len(self.vec[self.index]):
                    return True
                else:
                    self.index += 1
                    self.index2d = 0
            else:
                return True
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())