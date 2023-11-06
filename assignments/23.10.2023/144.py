class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        def preorder(root):
            if not root:
                return 
            list1.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return list1