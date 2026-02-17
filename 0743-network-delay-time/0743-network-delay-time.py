import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj=[[]for i in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        dist=[float('inf')]*(n+1)
        def dij(src):
            dist[src]=0
            pq=[]
            heapq.heappush(pq,(0,src))

            while pq:
                d,node=heapq.heappop(pq)
                if d>dist[node]:
                    continue
                for nei,weight in adj[node]:
                    if dist[node]+weight<dist[nei]:
                        dist[nei]=dist[node]+weight
                        heapq.heappush(pq,(dist[nei],nei))
            return dist
        dij(k)
        for i in range(1,len(dist)):
            if dist[i]==float('inf'):
                return -1
            
        maxi=max(dist[1:])
        return maxi
        # maxi = max(dist[1:])
        # if maxi == float('inf'):
        #     return -1
        # return maxi
