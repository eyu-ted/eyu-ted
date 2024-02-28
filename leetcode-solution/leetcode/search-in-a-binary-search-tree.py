# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:


        
        def traverse(root):
            if not root:
                return 
            if root.val>val:
                return traverse(root.left)
            elif root.val<val:
                return traverse(root.right)

            if root.val==val:
                return root

        return traverse(root)      