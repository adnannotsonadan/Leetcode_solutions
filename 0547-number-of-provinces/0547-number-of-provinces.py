class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # n=len(isConnected)
        # adj=[[] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j]==1:
        #             adj[i].append(j)
        #             adj[j].append(i)
        # def dfs(i):
        #     vis[i]=1
        #     for nei in adj[i]:
        #         if vis[nei]==0:
        #             dfs(nei)
            
        # vis=[0]*(n)
        # l=0
        # for i in range(n):
        #     if vis[i]==0:
        #         l+=1
        #         dfs(i)
        # return l
#         n=len(isConnected)
        
#         dsu=DSU(n)
#         for i in range(n):
#             for j in range(n):
#                 if isConnected[i][j]==1:
#                     dsu.unite(i,j)
#         return dsu.components

# class DSU:
#     def __init__(self,n):
#         self.parent=[i for i in range(n)]
#         self.size=[1]*(n)
#         self.components=n
#     def find(self,x):
#         if x==self.parent[x]:
#             return x
#         self.parent[x]=self.find(self.parent[x])
#         return self.parent[x]
#     def unite(self,u,v):
#         u=self.find(u)
#         v=self.find(v)

#         if u==v:
#             return False
#         if self.size[u]<self.size[v]:
#             u,v=v,u
#         self.parent[v]=u
#         self.size[u]+=self.size[v]
#         self.components-=1
#         return True



        # n=len(isConnected)
        # adj=[[] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j]==1 and i!=j:
        #             adj[i].append(j)
        #             adj[j].append(i)


        # vis=[0]*n

        # def dfs(src):
        #     vis[src]=1
        #     for nei in adj[src]:
        #         if not vis[nei]:
        #             dfs(nei)
        # cc=0
        # for i in range(n):
        #     if not vis[i]:
        #         cc+=1
        #         dfs(i)
        # return cc

        n=len(isConnected)
        m=len(isConnected[0])
        adj=[[]*n for _ in range(n)]
        vis=[0]*n

        for i in range(n):
            for j in range(m):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        
        def dfs(node):
            vis[node]=1
            for nei in adj[node]:
                if vis[nei]==0:
                    dfs(nei)
        
        cc=0
        for i in range(n):
            if vis[i]==0:
                cc+=1
                dfs(i)
        return cc