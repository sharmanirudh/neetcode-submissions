# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        order = []
        stack = [root]
        visited = set()
        while stack:
            node = stack[-1]
            if node.left and node.left not in visited:
                visited.add(node.left)
                stack.append(node.left)
                continue
            if not node.left or node.left in visited:
                visited.add(node)
                order.append(node.val)
                stack.pop()
                if node.right:
                    visited.add(node.right)
                    stack.append(node.right)

        return order