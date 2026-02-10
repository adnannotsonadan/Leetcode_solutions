class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(mat)
        m=len(mat[0])
        moves=[(-1,0),(1,0),(0,-1),(0,1)]

        def bfs():
            q=[]
            vis=[[0]*m for _ in range(n)]
            dist=[[-1]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if mat[i][j]==0:
                        dist[i][j]=0
                        vis[i][j]=1
                        q.append((i,j))
            while q:
                f1,f2=q.pop(0)
                for dx,dy in moves:
                    ni=f1+dx
                    nj=f2+dy
                    if ni>=0 and nj>=0 and ni<n and nj<m:
                        if vis[ni][nj]==0:
                            dist[ni][nj]=dist[f1][f2]+1
                            q.append((ni,nj))
                            vis[ni][nj]=1
            return dist
        return bfs()
            