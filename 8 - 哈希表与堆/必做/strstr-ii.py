class Solution:
    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index
    def strStr2(self, source, target):
        # Write your code here
        BASE = 1000000
        if source is None or target is None:
            return -1
        if target == '':
            return 0

        power = 1
        for i in range(len(target) - 1):
            power = (power * 31) % BASE

        targetHashCode = 0
        for i in range(len(target)):
            targetHashCode = (targetHashCode * 31 + ord(target[i])) % BASE

        sourceHashCode = 0
        for i in range(len(source)):
            if i < len(target):
                sourceHashCode = (sourceHashCode * 31 + ord(source[i])) % BASE
            else:
                toMinus = ord(source[i - len(target)]) * power
                sourceHashCode = (sourceHashCode - toMinus) % BASE
                sourceHashCode = (sourceHashCode * 31 + ord(source[i])) % BASE
                if sourceHashCode < 0:
                    sourceHashCode = (sourceHashCode + BASE) % BASE

            if i >= len(target) - 1 and sourceHashCode == targetHashCode:
                n = 0
                while source[n + i - len(target) + 1] == target[n]:
                    if n == len(target) - 1:
                        return i - len(target) + 1
                    n += 1
        return -1