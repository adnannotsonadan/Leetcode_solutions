class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans=1
        def p(x,n,ans):
            if n < 0:
                x = 1 / x
                n = -n

            if n==0:
                return ans
            if n%2==1:
                ans*=x
                n-=1
            else:
                x*=x
                n//=2
            return p(x,n,ans)
        return p(x,n,ans)
         