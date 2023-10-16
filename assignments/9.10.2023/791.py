class Solution:
    def customSortString(self, order: str, s: str) -> str:

        l = []
        for i in order:
            if i in s:

                while i in s:

                    l.append(i)
                    s.pop()

            else:
                break

        ans = ''.join(l)

        return ans
        