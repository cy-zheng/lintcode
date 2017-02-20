class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.cache = {}
        

    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        # Write your code here
        if number not in self.cache:
            self.cache[number] = 1
        else:
            self.cache[number] += 1


    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        for key in self.cache:
            if 2 * key == value:
                if self.cache[key] > 1:
                    return True
            else:
                if (value - key) in self.cache:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)