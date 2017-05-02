class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        if not chars:
            return chars
        left, right = 0, len(chars) - 1
        while left < right:
            if ord(chars[left]) <= 90:
                chars[left], chars[right] = chars[right], chars[left]
                right -= 1
            else:
                left += 1
        return chars
