from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # res=[]
        # if not root:
        #     return []
        # def lvl(node):
        #     l_to_r=True
        #     q=deque([root])
        #     while q:
        #         lvl_size=len(q)
        #         curr_lvl=[]
        #         for _ in range(lvl_size):
        #             f=q.popleft()
        #             curr_lvl.append(f.val)
        #             if f.left is not None:
        #                 q.append(f.left)
        #             if f.right is not None:
        #                 q.append(f.right)
        #         if l_to_r:
        #             res.append(curr_lvl)
        #             l_to_r=False
        #         elif not l_to_r:
        #             res.append(curr_lvl[::-1])
        #             l_to_r=True
        # lvl(root)
        # return res
        
        res=[]
        if not root:
            return []
        def solve(node):
            flag=False
            q=deque()
            q.append(node)
            while q:
                lvl=[]
                for i in range(len(q)):
                    e=q.popleft()
                    lvl.append(e.val)
                    if e.left:
                        q.append(e.left)
                    if e.right:
                        q.append(e.right)
                if flag==True:
                    lvl.reverse()
                res.append(lvl[:])
                flag=not flag
        solve(root)
        return res

