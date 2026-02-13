class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj=[[] for _ in range(numCourses)]
        res=[]
        indeg=[0]*(numCourses)
        for u,v in prerequisites:
            adj[v].append(u)
            indeg[u]+=1
        q=[]
        for i in range(len(indeg)):
            if indeg[i]==0:
                q.append(i)
        while q:
            f=q.pop(0)
            res.append(f)
            for nei in adj[f]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        if len(res)==numCourses:
            return True
        else:
            return False