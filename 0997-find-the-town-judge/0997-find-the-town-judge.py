class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # sol1
        # lst=[[]for _ in range(n+1)]
        # indeg=[0]*(n+1)
        # for u,v in trust:
        #     lst[u].append(v)
        #     indeg[v]+=1
        # for i in range(1,len(lst)):
        #     if len(lst[i])==0 and indeg[i]==n-1:
        #         return i
        # return -1

        # sol2
        # lst=[[] for _ in range(n+1)]
        # indeg=[0]*(n+1)
        # outdeg=[0]*(n+1)
        # for u,v in trust:
        #     lst[u].append(v)
        #     indeg[v]+=1
        # for i in range(1,n+1):
        #     outdeg[i]=len(lst[i])
        # for i in range(1,n+1):
        #     if indeg[i]==n-1 and outdeg[i]==0:
        #         return i
        # return -1

        # sol3
        mat=[[0]*(n+1) for _ in range(n+1)]
        indeg=[0]*(n+1)
        for u,v in trust:
            mat[u][v]=1
            indeg[v]+=1
        for i in range(1,n+1):
            if sum(mat[i])==0 and indeg[i]==(n-1):
                return i
        return -1