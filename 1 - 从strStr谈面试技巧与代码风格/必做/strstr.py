class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if target == '':
            return 0
        for i in range(len(source)):
            m = i
            n = 0
            while m < len(source) and source[m] == target[n]:
                if n == len(target) - 1:
                    return i
                m += 1
                n += 1
        return -1