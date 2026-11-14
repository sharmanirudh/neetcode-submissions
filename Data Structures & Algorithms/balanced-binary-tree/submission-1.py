# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_balanced = True
        def dfs(root):
            nonlocal is_balanced
            if not root:
                return 0
            left = right = 0
            if root.left:
                left = dfs(root.left)
                left += 1
            if root.right:
                right = dfs(root.right)
                right += 1
            if abs(left - right) > 1:
                is_balanced = False
            return max(left, right)

        dfs(root)
        return is_balanced

