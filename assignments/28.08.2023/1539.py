class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ar = []
        
        
        for i in range (0,2001):
            ar.append(i) 
        for j in range(0,len(ar)):

            if j in arr:
                ar.remove(j) 
       
        return ar[k]