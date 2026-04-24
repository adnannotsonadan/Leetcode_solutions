from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # n=len(grid)
        # m=len(grid[0])
        # vis=[[0]*m for _ in range(n)]
        # tm=0
        # moves=[(1,0),(0,1),(-1,0),(0,-1)]
        # q=deque()
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j]==2:
        #             q.append((i,j,0))    
        
        # while q:
        #     f1,f2,t=q.popleft()
        #     tm=max(tm,t)
        #     for di,dj in moves:
        #         ni=f1+di
        #         nj=f2+dj
        #         if ni>=0 and ni<n and nj>=0 and nj<m and grid[ni][nj]==1:
        #             if vis[ni][nj]==0:
        #                 vis[ni][nj]=1
        #                 grid[ni][nj]=2
        #                 q.append((ni,nj,t+1))
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j]==1:
        #             return -1
        # return tm

        n=len(grid)
        m=len(grid[0])
        q=deque()
        moves=[(1,0),(0,1),(-1,0),(0,-1)]
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    vis[i][j]=1
                    
        tm=0       
        while q:
            dx,dy,t=q.popleft()
            tm=max(t,tm)
            for f,l in moves:
                ni=f+dx
                nj=l+dy
                if ni>=0 and ni<n and nj>=0 and nj<m and grid[ni][nj]==1:
                    if not vis[ni][nj]:
                        vis[ni][nj]=1
                        q.append((ni,nj,t+1))
                        grid[ni][nj]=2
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return tm
