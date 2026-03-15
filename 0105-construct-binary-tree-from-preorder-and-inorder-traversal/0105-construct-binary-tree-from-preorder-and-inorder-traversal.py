# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        res=[]
        def rec(pre,ino):
            if not pre or not ino:
                return None
            root=TreeNode(pre[0])
            ind=ino.index(pre[0])
            root.left=rec(pre[1:ind+1],ino[:ind])
            root.right=rec(pre[ind+1:],ino[ind+1:])
            return root
        return rec(preorder,inorder)
        