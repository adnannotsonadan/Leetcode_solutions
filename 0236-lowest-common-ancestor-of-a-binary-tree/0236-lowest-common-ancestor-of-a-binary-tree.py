# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res=[]
        def post(node):
            if not node:
                return None

            l=post(node.left)
            r=post(node.right)
            if node==p or node==q:
                return node

            if  l and  r:
                return node  
            
            if l:
                return l
            if r:
                return r
            return None

        res=post(root)
        return res    