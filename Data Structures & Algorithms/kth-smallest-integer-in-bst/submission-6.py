# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = 0
        result = None
        def dfs(root):
            nonlocal seen, result
            if not root:
                return seen
            dfs(root.left)
            seen += 1
            if seen == k:
                result = root.val
            dfs(root.right)
        dfs(root)
        return result