class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        V = 0
        for u,v in edges:
            V = max(V, u, v)
        # adj=[[]for _ in range(V+1)]
        # vis=[0]*(V+1)

        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # def dfs(node,parent):
        #     q=[]
        #     vis[node]=1
        #     q.append((node,parent))
        #     while q:
        #         n,p=q.pop(0)
        #         for nei in adj[n]:
        #             if vis[nei]==0:
        #                 vis[nei]=1
        #                 q.append((nei,n))
        #             else:
        #                 if nei!=p:
        #                     return [n,nei]
            

        # for i in range(1,V+1):
        #     if vis[i]==0:
        #         ans=dfs(i,-1)
        #         if ans:
        #             return ans
        res=[]
        dsu=DSU(V)
        for u,v in edges:
            if not dsu.unite(u,v):
                res.append(u)
                res.append(v)
        return res
class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
        # self.components=n
    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def unite(self,a,b):
        a=self.find(a)
        b=self.find(b)

        if a==b:
            return False
        if self.size[a]<self.size[b]:
            a,b=b,a
        self.parent[b]=a
        self.size[a]+=self.size[b]
        # component-=1
        return True