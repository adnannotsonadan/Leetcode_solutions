class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def rec(n):
            if n<=1:
                return n
            return rec(n-2)+rec(n-1)
        return rec(n)