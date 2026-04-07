class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s)==0:
        #     return 0
        # sign=1
        # s=s.strip()
        # s = s.strip()
        # if not s:
        #     return 0

        # if s[0]=='-' or s[0]=='+':
        #     if s[0]=='-':
        #         sign=-1
        #     s=s[1:]
        # ld=0
        # for i in range(len(s)):
        #     if not s[i].isdigit():
        #         break
        #     ld=ld*10+int(s[i])
        # ld=ld*sign
        # if ld<-2**31:
        #     return -2**31
        # elif ld>2**31-1:
        #     return 2**31-1

        # return ld

        s=s.strip()
        if not s:
            return 0
        sign=1
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign=-1
            s=s[1:]
        def rec(s,ld,i):
            if i==len(s) or  not s[i].isdigit():
                return ld
            ld=ld*10+int(s[i])*sign
            if ld<-2**31:
                return -2**31
            elif ld>2**31-1:
                return 2**31-1

            return rec(s,ld,i+1)
        return rec(s,0,0)