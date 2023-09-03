class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in range(0, len(nums)):
            if nums[i] ==1:
                count = count + 1
            else:
                result =max(count,result)
                count = 0 

        return max(count,result) 