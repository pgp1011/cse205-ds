# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def func(arr):
            if len(arr)==0:return None
            cur=TreeNode(arr[0])
            t=len(arr)
            for i in range(1,len(arr)):
                if arr[i]>arr[0]:
                    t=i
                    break
            cur.left=func(arr[1:t])
            cur.right=func(arr[t:])
            return cur
        return func(preorder)
        