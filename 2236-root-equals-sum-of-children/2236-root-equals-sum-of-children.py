# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        s=0
        q=deque([root])
        while q:
            for i in range(len(q)):
                f=q.popleft()
                if f.left:
                    q.append(f.left)
                    s+=f.left.val
                if f.right:
                    q.append(f.right)
                    s+=f.right.val
        if s==root.val:
            return True
        return False