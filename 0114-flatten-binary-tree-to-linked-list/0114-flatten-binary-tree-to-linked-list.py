# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        prev=[None]
        def post(node):
            if not node:
                return None
            post(node.right)
            post(node.left)
            node.right=prev[0]
            node.left=None
            prev[0]=node
        return post(root)