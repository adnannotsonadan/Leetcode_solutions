class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        lst=[[]for _ in range(n+1)]
        indeg=[0]*(n+1)
        for u,v in trust:
            lst[u].append(v)
            indeg[v]+=1
        for i in range(1,len(lst)):
            if len(lst[i])==0 and indeg[i]==n-1:
                return i
        return -1
