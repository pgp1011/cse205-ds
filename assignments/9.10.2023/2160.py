class Solution:
    def minimumSum(self, num: int) -> int:

        arr = []

        s= str(num)
        for i in range(len(s)):
            arr.append(s[i])


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

        a = arr[0] + arr[2]
        b = arr[1] + arr[3]

        ans = int(a) + int(b)
        return ans
        