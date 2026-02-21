class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        vis=[[0]*m for _ in range(n)]
        def bfs(si,sj,t):
            q=[]
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==2:
                        vis[i][j]=2
                        q.append((i,j,0))
                    # else:
                    #     vis[i][j]=0
            tm=0
            while q:
                f1,f2,t=q.pop(0)
                tm=max(tm,t)
                for dx,dy in moves:
                    ni=dx+f1
                    nj=dy+f2
                    if ni>=0 and ni<n and nj>=0 and nj<m and grid[ni][nj]==1:
                        if vis[ni][nj]==0: 
                            vis[ni][nj]=1
                            grid[ni][nj]=2
                            q.append((ni,nj,t+1))
            for i in range(n):
                for j in range(m):
                    if vis[i][j]!=2 and grid[i][j]==1:
                        return -1
            return tm
        return bfs(0,0,0)
            