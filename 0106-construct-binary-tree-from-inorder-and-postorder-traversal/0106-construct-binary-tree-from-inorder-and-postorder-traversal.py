# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        n=len(inorder)
        def rec(post,ino):
            if not post or not ino:
                return None
            root=TreeNode(post[-1])
            ind=ino.index(post[-1])
            root.left=rec(post[:ind],ino[:ind])
            root.right=rec(post[ind:-1],ino[ind+1:])
            return root
        return rec(postorder,inorder)