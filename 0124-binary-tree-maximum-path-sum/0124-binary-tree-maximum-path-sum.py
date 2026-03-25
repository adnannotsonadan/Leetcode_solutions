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
        # self.maxi=float('-inf')
        # def mp(node):
        #     if not node:
        #         return 0
        #     l=mp(node.left)
        #     if l<0:
        #         l=0
        #     r=mp(node.right)
        #     if r<0:
        #         r=0
        #     self.maxi=max(self.maxi,l+node.val+r)
        #     return node.val+max(l,r)
        # mp(root)
        # return self.maxi
        maxi=[float('-inf')]
        def mp(node):
            if not node:
                return 0
            left=mp(node.left)
            if left<0:
                left=0
            right=mp(node.right)
            if right<0:
                right=0
            maxi[0]=max(maxi[0],left+node.val+right)
            return node.val+max(left,right)
        mp(root)
        return maxi[0]