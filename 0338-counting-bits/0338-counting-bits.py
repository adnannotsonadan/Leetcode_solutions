class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]*(n+1)

        for i in range(n+1):
            if i%2==1:
                res[i]=res[i//2]+1
            else:
                res[i]=res[i//2]
        return res