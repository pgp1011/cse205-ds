class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        arr = []
        for i in range(l):
            if nums[i] not in arr:
                arr.append(nums[i])
            else:
                rep = nums[i]

        sum1 = l*(l+1)//2
        sum2 = sum(arr)

        miss = sum1 - sum2
        return [ rep , miss]
        