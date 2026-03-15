# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict,deque
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent=defaultdict(int)

        def dfs(node):
            if not node:
                return None
            if node.left:
                parent[node.left]=node
            dfs(node.left)
            dfs(node.right)
            if node.right:
                parent[node.right]=node
        dfs(root)
        ans=[]
        def bfs(node):
            q=deque([target])
            c=0
            vis=set([target])
            while q:
                if c==k:
                    for node in q:
                        ans.append(node.val)
                    return ans
                for i in range(len(q)):
                    f=q.popleft()
                    if f.left and f.left not in vis:
                        q.append(f.left)
                        vis.add(f.left)
                    if f.right and f.right not in vis:
                        q.append(f.right)
                        vis.add(f.right)
                    if f in parent and parent[f] not in vis:
                        q.append(parent[f])
                        vis.add(parent[f])
                c+=1
            return ans
                    
        return bfs(target)
        
        