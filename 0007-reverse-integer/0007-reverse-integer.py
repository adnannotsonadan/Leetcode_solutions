class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=x
        b=1
        if r<0:
            r=-r
            b=-1
        n=0
        while r:
            ld=r%10
            n=n*10+ld
            r=r//10
        y = n*b
        if y<-2**31 or y>2**31 - 1:
            return 0
        return y
        
