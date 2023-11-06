# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        values = []
        self.inorder(root, nodes, values)
        values.sort()
        for i in range(len(nodes)):
            nodes[i].val = values[i]       
    def inorder(self, root, nodes, values):
        if root:
            self.inorder(root.left, nodes, values)
            nodes.append(root)
            values.append(root.val)
            self.inorder(root.right, nodes, values)
        