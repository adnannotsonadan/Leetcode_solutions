# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans=[]
        q=deque([(root,0)])
        while q:
            temp=[]
            for _ in range(len(q)):
                f,c=q.popleft()
                if not f:
                    continue
                temp.append(f.val)
  
                if f.left:
                    q.append((f.left,c-1))
                if f.right:
                    q.append((f.right,c+1))
            if temp:
                ans.append(temp[-1])
        return ans

        