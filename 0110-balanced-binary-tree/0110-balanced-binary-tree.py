# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dep(node):
            if not node:
                return 0
            lf=dep(node.left)
            if lf==-1:
                return -1
            rg=dep(node.right)
            if rg==-1:
                return -1
            if abs(lf-rg)>1:
                return -1
            return 1 + max(lf,rg)
        x = dep(root)
        if x==-1:
            return False
        return True