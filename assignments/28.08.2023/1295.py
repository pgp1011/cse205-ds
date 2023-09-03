class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        
        count2 =0
        
        for i in range(0,len(nums)):
            count = 0
            while nums[i] > 0:
                nums[i] = nums[i] // 10
                count= count +1
                 

            if count%2 ==0: 
                count2 = count2+1

        return count2