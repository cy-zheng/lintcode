class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        if s == "":
            return True
        elif not dict:
            return False
        flag = [False] * (len(s) + 1)
        flag[0] = True
        maxLength = max([len(w) for w in dict])
        for i in xrange(1, len(flag)):
            for j in xrange(i - 1, -1, -1):
                if i - j > maxLength:
                    break
                if flag[j] and s[j:i] in dict:
                    flag[i] = True
                    break
        return flag[-1]
        