class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            
            curr_max = max(nums[i], curr_max + nums[i])
            largest = max(largest, curr_max)

        return largest