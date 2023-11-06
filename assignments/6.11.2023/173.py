# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    st=[]
    def __init__(self, root: Optional[TreeNode]):
        self.pushall(root)

    def next(self) -> int:
        temp=self.st.pop()
        self.pushall(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return True if len(self.st)>0 else False

    def pushall(self,root):
        while root:
            self.st.append(root)
            root=root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()