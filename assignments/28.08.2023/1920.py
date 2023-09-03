class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        x=0
        for i in range(0,len(nums)):
            
            x = nums[nums[i]]
            ans[i]=x

        return ans            