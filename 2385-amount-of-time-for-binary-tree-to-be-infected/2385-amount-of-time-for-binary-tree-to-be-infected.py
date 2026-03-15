# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        parent={}
        def dfs(node):
            if not node:
                return None
            if node.left:
                parent[node.left]=node
            dfs(node.left)
            if node.right:
                parent[node.right]=node
            dfs(node.right)
        dfs(root)
        def find(node):
            if not node:
                return None
            if node.val==start:
                return node
            l=find(node.left)
            if l:
                return l
            r=find(node.right)
            if r:
                return r
        start_node=find(root)
        def bfs(node):
            q=deque([node])
            c=0
            vis=set([node])
            while q:
                inf=False
                for i in range(len(q)):
                    f=q.popleft()
                    if f.left and f.left not in vis:
                        q.append(f.left)
                        vis.add(f.left)
                        inf=True
                    if f.right and f.right not in vis:
                        q.append(f.right)
                        vis.add(f.right)
                        inf=True
                    if f in parent and parent[f] not in vis:
                        q.append(parent[f])
                        vis.add(parent[f])
                        inf=True
                if inf:
                    c+=1
            return c
        return bfs(start_node)
                
                