from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        q=deque()
        moves=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    vis[i][j]=1
        tm=0
        while q:
            f,l,t=q.popleft()
            tm=max(tm,t)
            for dx,dy in moves:
                ni=dx+f
                nj=dy+l
                if ni>=0 and ni<n and nj>=0 and nj<m and grid[ni][nj]==1:
                    q.append((ni,nj,t+1))
                    vis[ni][nj]=1
                    grid[ni][nj]=2
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return tm