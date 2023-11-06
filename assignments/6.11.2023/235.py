# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        data=root.val
        if data>p.val and data>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if data<p.val and data<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root