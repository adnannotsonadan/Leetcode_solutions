class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(mat)
        m=len(mat[0])
        vis=[[0]*m for _ in range(n)]
        dist=[[0]*m for _ in range(n)]
        q=[]
        moves=[[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    vis[i][j]=1
                    dist[i][j]=0
        while q:
            f1,f2,d=q.pop(0)
            for dx,dy in moves:
                ni=dx+f1
                nj=dy+f2

                if ni>=0 and ni<n and nj>=0 and nj<m:
                    if vis[ni][nj]==0:
                        vis[ni][nj]=1
                        dist[ni][nj]=d+1
                        q.append((ni,nj,d+1))
        return dist