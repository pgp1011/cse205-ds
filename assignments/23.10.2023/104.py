# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        level = 0

        list1 = [root]
        while list1:

            row = []
            for i in range(len(list1)):
                node = list1.pop(0)
                if node.left:
                    list1.append(node.left)
                if node.right:
                    list1.append(node.right)

            level += 1
           
        return level