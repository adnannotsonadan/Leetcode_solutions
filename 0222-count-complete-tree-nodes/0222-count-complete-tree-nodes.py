# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        res=[]
        q=deque([root])
        res.append(root.val)
        while q:
            for i in range(len(q)):
                f=q.popleft()
                if f.left:
                    q.append(f.left)
                    res.append(f.left.val)
                if f.right:
                    q.append(f.right)
                    res.append(f.right.val)
        return len(res)