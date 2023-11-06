# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        def postorder(root):
            
            if not root:
                return 
            
            postorder(root.left)       
            postorder(root.right)
            list1.append(root.val)  
            
        postorder(root)
        return list1