# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
    
        def insert(root: TreeNode, val: int, depth: int, ind: int):
            if root == None:
                return

            if depth - 1 == ind:
                root.left = TreeNode(val, root.left, None) 
                root.right = TreeNode(val, None, root.right)

            insert(root.left, val, depth, ind + 1)
            insert(root.right, val, depth, ind + 1)
            return

        insert(root, val, depth, 1)

        return root
        