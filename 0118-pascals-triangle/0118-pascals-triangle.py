class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[]
        matrix.append([1])
        matrix.append([1,1])
        if numRows==1:
            return [matrix[0]]
        if numRows==2:
            return [matrix[0],matrix[1]]
        for i in range(3,numRows+1):
            res=[]
            for j in range(0,i):
                if j==0 or j==i-1:
                    res.append(1)
                elif 0<j<i-1:
                    res.append(matrix[i-2][j-1]+matrix[i-2][j])
                    
            matrix.append(res[:])
        return matrix
        