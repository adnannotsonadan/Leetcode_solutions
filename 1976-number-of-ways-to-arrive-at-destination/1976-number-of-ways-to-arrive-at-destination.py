import heapq
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD=10 ** 9 +7
        adj=[[] for _  in range(n)]
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist=[float('inf')]*n
        ways=[0]*n
        def dij(src):
            dist[src]=0
            ways[src]=1
            pq=[]
            heapq.heappush(pq,(0,src))
            while pq:
                d,node=heapq.heappop(pq)
                if d>dist[node]:
                    continue
                for nei, weight in adj[node]:
                    new_dist=d+weight
                    if new_dist<dist[nei]:
                        dist[nei]=new_dist
                        ways[nei]=ways[node]
                        heapq.heappush(pq,(dist[nei],nei))
                    elif new_dist==dist[nei]:
                        ways[nei]+=ways[node]
            return ways[n-1]%MOD
        return dij(0)
                    