class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        vis=[0]*n
        
        adj=[[] for _ in range(n)]    
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            vis[node]=1
            for nei in adj[node]:
                if vis[nei]==0:
                    dfs(nei)
        cc=0
        if len(connections)<n-1:
            return -1
        
        for i in range(n):
            if vis[i]==0:
                cc+=1
                dfs(i)
        return cc-1    