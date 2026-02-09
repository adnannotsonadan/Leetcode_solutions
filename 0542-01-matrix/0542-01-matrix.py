class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(mat)
        m=len(mat[0])
        moves=[[-1,0],[1,0],[0,-1],[0,1]]
        dist=[[-1]*m for _ in range(n)]
        q=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j))
                    dist[i][j]=0
        while q:
            f1,f2=q[0]
            q.pop(0)

            for dx,dy in moves:
                ni=f1+dx
                nj=f2+dy
                if ni>=0 and ni<n and nj>=0 and nj<m:
                    if dist[ni][nj]==-1:
                        dist[ni][nj]=dist[f1][f2]+1
                        q.append((ni,nj))
        return dist
            