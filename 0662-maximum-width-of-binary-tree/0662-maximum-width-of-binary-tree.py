# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi=float('-inf')
        q=deque([(root,0)])
        while q:
            first = q[0][1]
            last = q[-1][1]
            for i in range(len(q)):
                f,ind=q.popleft()
                if f.left:
                    q.append((f.left,(2*ind)+1))
                if f.right:
                    q.append((f.right,(2*ind)+2))
            maxi=max(maxi,last-first+1)
        return maxi
        