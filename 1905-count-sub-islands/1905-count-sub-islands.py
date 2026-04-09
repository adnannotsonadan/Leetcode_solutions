class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        n1=len(grid1)
        m1=len(grid1[0])

        n2=len(grid2)
        m2=len(grid2[0])

        count=0
        found=[True]
      

        def dfs(r,c):
         
            if r<0 or c<0 or r>=n2 or c>=m2 or grid2[r][c]==0:
                return
            if grid1[r][c]==0:
                found[0]=False
            grid2[r][c]=0
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        for i in range(n1):
            for j in range(m1):
                if grid2[i][j]==1:
                    found=[True]
                    print("called")
                    dfs(i,j)
                    if found[0]:
                        count+=1
        return count