# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        return self.maxDepth(root)[0]
    
    def maxDepth(self,root):

        if not root:
            return [True, 0]

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
            
        bal = left_depth[0] and right_depth[0] and abs(left_depth[1] - right_depth[1]) <= 1
            
                
        return [bal, 1 + max(left_depth[1],right_depth[1])]

        

        

