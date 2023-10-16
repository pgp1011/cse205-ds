class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        L = len(arr)
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

        Merge_Sort(arr)
        diff = arr[1] - arr[0]
        for i in range(L-1):
            if (arr[i] > 0 and arr[i+1] > 0) or (arr[i] < 0 and arr[i+1] < 0) or (arr[i] < 0 and arr[i+1] >0):
                mini = arr[i+1] - arr[i]
                diff = min(mini,diff)
                

        ans = []
        for i in range(L-1):
            temp = []
            if (arr[i+1] - arr[i]) == diff:
                temp.append(arr[i])
                temp.append(arr[i+1])

                ans.append(temp)

        return ans

            

        