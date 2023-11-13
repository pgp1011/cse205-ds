class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return (nums[0] - 1) * (nums[1] - 1)

        heap = [nums[0], nums[1]]
        heapify(heap)
        for num in nums[2:]:            
            heappushpop(heap, num)

        return (heap[0] - 1) * (heap[1] - 1)