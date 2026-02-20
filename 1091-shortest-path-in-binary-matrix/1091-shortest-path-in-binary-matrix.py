class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0]==1:
            return -1
        n=len(grid)
        moves=[[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,-1],[1,-1],[-1,1]]
        vis=[[0]*n for _ in range(n)]
        def bfs(si,sj,dist):
            vis[si][sj]=1
            q=[]
            q.append((si,sj,dist))
            while q:
                f1,f2,dist=q.pop(0)
                if f1==n-1 and f2==n-1:
                    return dist
                for dx,dy in moves:
                    ni=f1+dx
                    nj=f2+dy
                    if ni>=0 and ni<n and nj>=0 and nj<n and grid[ni][nj]==0:
                        if vis[ni][nj]==0:
                            vis[ni][nj]=1
                            q.append((ni,nj,dist+1))
            return -1
        return bfs(0,0,1)
        