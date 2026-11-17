# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def path_to_node(root, node, path=None):
            path = path or []
            if not root:
                return path
            path.append(root)
            if root.val == node.val:
                return path
            if node.val < root.val:
                path = path_to_node(root.left, node, path)
                return path
            if node.val > root.val:
                path = path_to_node(root.right, node, path)
                return path

        path_to_p = path_to_node(root, p)
        path_to_q = path_to_node(root, q)
        path_to_p = path_to_p[::-1]
        path_to_q = path_to_q[::-1]
        print(repr(path_to_p))
        print(repr(path_to_q))
        result = path_to_p.pop()
        path_to_q.pop()
        while path_to_p and path_to_q:
            an_p = path_to_p.pop()
            an_q = path_to_q.pop()
            if an_p.val == an_q.val:
                result = an_p
            else:
                break
        return result