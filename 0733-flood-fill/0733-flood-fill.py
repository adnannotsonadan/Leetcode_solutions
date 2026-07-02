class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # n=len(image)
        # m = len(image[0])
        # clr=image[sr][sc]
        # if clr==color:
        #     return image
        # def dfs(i,j):
        #     image[i][j]=color
        #     if i>0 and image[i-1][j]==clr:
        #         dfs(i-1,j)
        #     if i<n-1 and image[i+1][j]==clr:
        #         dfs(i+1,j)
        #     if j>0 and image[i][j-1]==clr:
        #         dfs(i,j-1)
        #     if j<m-1 and image[i][j+1]==clr:
        #         dfs(i,j+1)
        # dfs(sr,sc)
        # return image


        n = len(image)
        m = len(image[0])

        clr = image[sr][sc]

        if clr == color:
            return image

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # Up, Down, Left, Right

        def dfs(i, j):
            image[i][j] = color

            for dr, dc in moves:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == clr:
                    dfs(nr, nc)

        dfs(sr, sc)

        return image