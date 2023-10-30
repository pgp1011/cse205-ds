class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        while len(nums) > k:
            m = min(nums)
            nums.remove(m)

        return nums