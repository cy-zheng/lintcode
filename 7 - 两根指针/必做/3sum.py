class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        numbers.sort()
        i = 0
        while i < len(numbers):
            left = i + 1
            right = len(numbers) - 1
            while left < right:
                if numbers[right] + numbers[left] + numbers[i] == 0:
                    result.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < len(numbers) and numbers[left] == numbers[left - 1]:
                        left += 1
                    while right >= i + 1 and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif numbers[right] + numbers[left] + numbers[i] > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
            while i > 0 and i < len(numbers) and numbers[i] == numbers[i - 1]:
                i += 1
        return result