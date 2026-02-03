class Solution(object):
    def findCenter(self, edges):
        # freq = {}

        # for u, v in edges:
        #     freq[u] = freq.get(u, 0) + 1
        #     freq[v] = freq.get(v, 0) + 1

        # for node in freq:
        #     if freq[node] == len(edges):
        #         return node

        # n=len(edges)+1
        # mat = [[0]* (n+1) for _ in range(n+1)]
        # for u, v in edges:
        #     mat[u][v] = 1
        #     mat[v][u] = 1
        # for i in range(1, n+1):
        #     if sum(mat[i]) == n - 1:
        #         return i

        n = len(edges) + 1
        mat = [[] for _ in range(n+1)]

        for u, v in edges:
            mat[u].append(v)
            mat[v].append(u)

        for i in range(1, n+1):
            if len(mat[i]) == n - 1:
                return i