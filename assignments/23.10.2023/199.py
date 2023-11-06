# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = [root]
        res =[]

        while ans:

            t = ans.copy()
            ans.clear()
            r = 0

            for i in t:
                
                if i.left:
                    ans.append(i.left)
                if i.right:
                    ans.append(i.right)

                r = i.val
            
            res.append(r)

        return res

                

