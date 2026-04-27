# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # maxh=[0]
        # def dfs(node,maxh):
        #     if node==None:
        #         return 0
        #     lef=dfs(node.left,maxh)
        #     right=dfs(node.right,maxh)
        #     maxh[0]=max(lef+right,maxh[0])
        #     return (max(lef,right)+1)
        # dfs(root,maxh)
        # return maxh[0]

        dia=[0]
        def solve(node):
            if not node:
                return 0
            lefth=solve(node.left)
            righth=solve(node.right)
            dia[0]=max(dia[0],lefth+righth)
            return 1+max(lefth,righth)
        solve(root)
        return dia[0]