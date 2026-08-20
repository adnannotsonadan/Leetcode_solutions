class Solution:
    def addDigits(self, num: int) -> int:
        def rec(num):
            ans=0
            while num:
                ld=num%10
                ans+=ld
                num//=10
            return ans


        while num>=10:
            num=rec(num)
        return num