# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans=[0]
        def pre(node,isleft):
            
            if not node:
                return None
            if isleft and not node.left and not node.right:
                ans[0]+=node.val
            l=pre(node.left,True)
            r=pre(node.right,False)
        pre(root,False)
        return ans[0]