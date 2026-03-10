# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        def preorder(node,res):
            if node==None:
                return
            stack=[]
            stack.append(node)
            while stack:
                f=stack.pop()
                res.append(f.val)
                if f.right is not None:
                    stack.append(f.right)
                if f.left is not None:
                    stack.append(f.left)
        preorder(root,res)
        return res