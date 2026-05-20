class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        m=len(isConnected[0])

        adj=[[] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        vis=[0]*n
        def dfs(node):
            vis[node]=1
            for nei in adj[node]:
                if not vis[nei]:
                    dfs(nei)
        c=0
        for i in range(n):
            if not vis[i]:
                c+=1
                dfs(i)
        return c
