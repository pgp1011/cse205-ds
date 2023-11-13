class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = collections.Counter(hand)
        minHeap = [key for key in count.keys()]
        heapq.heapify(minHeap)
        while minHeap:
                first =  minHeap[0]
                for i in range(first, first+groupSize):
                    if i not in count:
                       return False
                    count[i] -= 1
                    if count[i] == 0:
                        heapq.heappop(minHeap)             
        return True
        