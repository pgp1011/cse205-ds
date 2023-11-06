# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return []

        list1 = [root]
        while list1:

            row = []
            for i in range(len(list1)):
                node = list1.pop(0)
                if node.left:
                    list1.append(node.left)
                if node.right:
                    list1. append(node.right)

                row.append(node.val)
            res.append(row)

        return res    



        
        