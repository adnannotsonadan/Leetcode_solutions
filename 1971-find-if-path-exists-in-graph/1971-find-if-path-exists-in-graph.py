class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        res=[]
        vis=[0]*n
        def dfs(node):
            vis[node]=1
            res.append(node)
            for j in adj[node]:
                if vis[j]==0:
                    dfs(j)
        dfs(source)
        if vis[destination]==1:
            return True
        else:
            return False