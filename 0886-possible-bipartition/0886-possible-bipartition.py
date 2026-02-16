class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adj=[[] for _ in range(n+1)]
        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        
        color=[-1]*(n+1)

        for i in range(1,n+1):
            if color[i]==-1:
                q=[]
                q.append(i)
                color[i]=0

                while q:
                    node=q.pop(0)
                    for nei in adj[node]:
                        if color[nei]==-1:
                            color[nei]=1-color[node]
                            q.append(nei)
                        elif color[nei]==color[node]:
                            return False
        return True