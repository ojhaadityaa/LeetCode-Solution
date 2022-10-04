# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return
        
        if root.left == None and root.right == None:
            if targetSum == root.val:
                return True
            return 
        
        a , b = None, None
        if root.left:
            a = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            b = self.hasPathSum(root.right, targetSum - root.val)
        return a or b
        