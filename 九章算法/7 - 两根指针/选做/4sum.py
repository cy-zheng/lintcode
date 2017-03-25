class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self, numbers, target):
        # write your code here
        numLen, res, d = len(numbers), set(), {}
        if numLen < 4: return []
        numbers.sort()
        for p in xrange(numLen):
            # Remove duplicate elements
            if p != numbers.index(numbers[p]):
                continue
            for q in xrange(p + 1, numLen): 
                if q > numbers.index(numbers[q]) + 1:
                    continue
                if numbers[p] + numbers[q] not in d:
                    d[numbers[p] + numbers[q]] = [[p, q]]
                else:
                    d[numbers[p] + numbers[q]].append([p, q])
        for p in xrange(numLen):
            for q in xrange(p + 1, numLen): 
                if (target - numbers[p] - numbers[q]) in d:
                    for pairs in d[target - numbers[p] - numbers[q]]:
                        if p in pairs or q in pairs:
                            continue
                        temp = [numbers[i] for i in pairs] + [numbers[p], numbers[q]]
                        temp.sort()
                        res.add(tuple(temp))
        return [list(i) for i in res]   
