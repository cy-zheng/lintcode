class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i in range(len(numbers)):
            numbers[i] = (numbers[i], i)
        numbers.sort(key=lambda x: x[0])
        left, right = 0, len(numbers) - 1
        while left < right:
            temp = numbers[left][0] + numbers[right][0]
            if temp < target:
                left = left + 1
            elif temp > target:
                right = right - 1
            else:
                return sorted([numbers[left][1] + 1, numbers[right][1] + 1])