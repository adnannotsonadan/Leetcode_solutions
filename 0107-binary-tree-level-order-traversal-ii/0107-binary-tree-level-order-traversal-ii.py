# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=deque([root])
        res=[]
        while q:
            lvl=[]
            for i in range(len(q)):
                f=q.popleft()
                if not f:
                    continue
                lvl.append(f.val)
                if f.left:
                    q.append(f.left)
                if f.right:
                    q.append(f.right)
            res.append(lvl[:])
        
        return res[::-1]
        