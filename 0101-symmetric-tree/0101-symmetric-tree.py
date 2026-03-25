# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        # def lvlOrder(left,right):
        #     if left==None and right==None:
        #         return True
        #     if left==None or right==None:
        #         return False
        #     if left.val!=right.val:
        #         return False
        #     l=lvlOrder(left.left,right.right)
        #     r=lvlOrder(left.right,right.left)
        #     return l and r
        # return lvlOrder(root.left,root.right)
        def sym(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            l=sym(left.left,right.right)
            r=sym(left.right,right.left)
            return l and r
        return sym(root.left,root.right)
