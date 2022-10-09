# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nums = set()
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root:
            if k - root.val in self.nums:
                return True
            else:
                self.nums.add(root.val)
            return self.findTarget(root.left, k) or self.findTarget(root.right, k)
        else:
            return False
        