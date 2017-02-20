class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s):
        # Write your code here
        if not s:
            return ''
        stack = []
        i = 0
        temp = 0
        while i < len(s):
            if self.isNum(s[i]):
                temp *= 10
                temp += int(s[i])
                i += 1
            elif s[i] == '[':
                stack.append(temp)
                temp = 0
                i += 1
            elif s[i] == ']':
                j = len(stack) - 1
                while not type(stack[j]) is int:
                    j -= 1
                exp = list(''.join(stack[j + 1:]) * stack[j])
                stack = stack[:j] + exp
                i += 1
            else:
                stack.append(s[i])
                i += 1
        return ''.join(stack)
        
    def isNum(self, s):
        if ord(s) in range(ord('0'), ord('9') + 1):
            return True
        return False