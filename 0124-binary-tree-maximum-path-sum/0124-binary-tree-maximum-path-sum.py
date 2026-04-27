# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi=[0]
        def solve(node):
            if not node:
                return 0
            lh=solve(node.left)
            if lh<0:
                lh=0
            rh=solve(node.right)
            if rh<0:
                rh=0
            maxi[0]=max(maxi[0],node.val+rh+lh)
            return node.val+max(lh,rh)
        solve(root)
        return maxi[0]