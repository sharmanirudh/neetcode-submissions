# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        def dfs(root, max_in_path):
            if not root:
                return
            if max_in_path <= root.val:
                result.append(root.val)
                max_in_path = root.val
            dfs(root.left, max_in_path)
            dfs(root.right, max_in_path)
        dfs(root, root.val)
        return len(result)