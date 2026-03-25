# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # if not root:
        #     return []
        # q=deque([root])
        # res=[]
        # while q:
        #     lvl=[]
        #     for i in range(len(q)):
        #         f=q.popleft()
        #         if not f:
        #             continue
        #         lvl.append(f.val)
        #         if f.left:
        #             q.append(f.left)
        #         if f.right:
        #             q.append(f.right)
        #     res.append(lvl[:])
        
        # return res
        res=[]
        if not root:
            return []
        q=deque([root])
        trav=True
        while q:
            lvl=[]
            for i in range(len(q)):
                node=q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if trav:
                res.append(lvl[:])
            else:
                res.append(lvl[::-1])
            trav=not trav
        return res
