class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        self.queue2.append(x)

    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        self.queue1 = self.queue2[::-1]
        x = self.queue1.pop(0)
        self.queue2 = self.queue1[::-1]
        return x

    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        return self.queue2[-1]

    # @return an boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return len(self.queue2) == 0