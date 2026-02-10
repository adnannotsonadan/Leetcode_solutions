class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        def bfs():
            q=[]
            vis=[[0]*m for _ in range(n)]
            dist=[[-1]*m for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    if grid[i][j]==2:
                        q.append((i,j))
                        vis[i][j]=1
                        dist[i][j]=0

            while q:
                f1,f2=q.pop(0)
                for dx,dy in moves:
                    new_i=dx+f1
                    new_j=dy+f2
                    if new_i>=0 and new_i<n and new_j>=0 and new_j<m:
                        if vis[new_i][new_j]==0 and grid[new_i][new_j]==1:
                            vis[new_i][new_j]=1
                            q.append((new_i,new_j))
                            dist[new_i][new_j]=dist[f1][f2]+1
            max_value=0
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1 and dist[i][j]==-1:
                        return -1
                    else:
                        max_value=max(max_value,dist[i][j])

            return max_value
        return bfs()
            