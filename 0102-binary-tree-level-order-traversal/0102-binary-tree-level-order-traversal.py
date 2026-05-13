from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        q=deque([])
        q.append(root)
        while q:
            temp=[]
            for i in range(len(q)):
                f=q.popleft()
                temp.append(f.val)
                if f.left is not None:
                    q.append(f.left)
                if f.right is not None:
                    q.append(f.right)
            res.append(temp[:])
        return res
