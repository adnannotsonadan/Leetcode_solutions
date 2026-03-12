
from collections import defaultdict
from collections import deque
# from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # code here
        m=defaultdict(list)
        q=deque([(root,0,0)])
        ans=[]
        if not root:
            return []
        while q:
            f,col,row=q.popleft()
            m[col].append((row,f.val))
            if f.left :
                q.append((f.left,col-1,row+1))
            if f.right:
                q.append((f.right,col+1,row+1))
        for key in sorted(m):
            temp = sorted(m[key])
            ans.append([val for row,val in temp])
        return ans