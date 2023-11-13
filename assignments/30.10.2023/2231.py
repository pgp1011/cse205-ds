class Solution:
    def largestInteger(self, num: int) -> int:
        from heapq import heappop, heappush, heapify

        heap1 = []
        heap2 = []

        for i in str(num):
            if int(i)%2:
                heap2.append(-int(i))
            else:
                heap1.append(-int(i))

        heapify(heap1)
        heapify(heap2)
        res = 0

        for i in str(num):
            if int(i)%2:
                res += -heappop(heap2)
                res *= 10
            else:
                res += -heappop(heap1)
                res *= 10 

        return res//10