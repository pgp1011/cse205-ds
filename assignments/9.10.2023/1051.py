class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        L = len(heights)
        h =[0]*L
        for i in range(L):
            h[i]= heights[i]
        def Merge_Sort(array):
            if len(array) > 1:
        #  mid is the point where the array is divided into two subarrays
                mid = len(array)//2
                Left = array[:mid]
                Right = array[mid:]

                Merge_Sort(Left)
                Merge_Sort(Right)

                i = j = k = 0

                while i < len(Left) and j < len(Right):
                    if Left[i] < Right[j]:
                        array[k] = Left[i]
                        i += 1
                    else:
                        array[k] = Right[j]
                        j += 1
                    k += 1

                while i < len(Left):
                    array[k] = Left[i]
                    i += 1
                    k += 1

                while j < len(Right):
                    array[k] = Right[j]
                    j += 1
                    k += 1


                while j < len(Right):
                    array[k] = Right[j]
                    j += 1
                    k += 1  
            return array
        new = Merge_Sort(heights)
        count = 0
        for i in range(L):

            if h[i] != new[i]:
                count +=1

        return count
