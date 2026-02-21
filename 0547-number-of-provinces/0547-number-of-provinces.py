class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        adj=[[] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        def dfs(i):
            vis[i]=1
            for nei in adj[i]:
                if vis[nei]==0:
                    dfs(nei)
            
        vis=[0]*(n+1)
        l=0
        for i in range(n):
            if vis[i]==0:
                l+=1
                dfs(i)
        return l