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
        self.maxi=float('-inf')
        def mp(node):
            if not node:
                return 0
            l=mp(node.left)
            if l<0:
                l=0
            r=mp(node.right)
            if r<0:
                r=0
            self.maxi=max(self.maxi,l+node.val+r)
            return node.val+max(l,r)
        mp(root)
        return self.maxi