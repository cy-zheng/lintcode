import string
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        s = s.lower()
        s = s.replace(" ", "")
        for word in string.punctuation:
            s = s.replace(word, "")
        return s == s[::-1]