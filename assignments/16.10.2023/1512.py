class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = 0
        d = {}

        for i in nums:
            if i in d:
                count += d[i]
                d[i] += 1
            else:
                d[i] = 1

        return count

        