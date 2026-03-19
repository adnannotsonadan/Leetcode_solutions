class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)

        #  matrix tp adj list conv
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)

        
        vis = [0] * n

        def dfs(i):
            vis[i] = 1
            for nei in adj[i]:
                if vis[nei] == 0:
                    dfs(nei)

        
        cc = 0
        for i in range(n):
            if vis[i] == 0:
                cc += 1
                dfs(i)

        return cc
