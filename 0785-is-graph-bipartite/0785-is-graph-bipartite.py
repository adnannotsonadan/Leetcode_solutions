class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color=[-1]*(len(graph))
        for i in range(len(graph)):
            if color[i]==-1:
                q=[]
                q.append(i)
                color[i]=0
                while q:
                    node=q.pop(0)
                    for nei in graph[node]:
                        if color[nei]==-1:
                            color[nei]=1-color[node]
                            q.append(nei)
                        elif color[nei]==color[node]:
                            return False
        return True 