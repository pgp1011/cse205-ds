class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:

            if i in d:
                rep = i
                d[i] += 1
                           
            else:
                d[i] = 1

        for j in range(1,len(nums)+1):

            if j not in d:
                miss = j

        return [rep, miss]