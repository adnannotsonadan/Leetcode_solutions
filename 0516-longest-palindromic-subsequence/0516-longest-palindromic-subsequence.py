class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pal=[]
        # def isPal(ans):
        #     if ans==ans[::-1]:
        #         pal.append(ans)
        # temp=[]
        # def rec(ind,ans):
        #     if ind==len(s):
        #         temp.append(ans)
        #         return
        #     ans.join(s[ind])
        #     rec(ind + 1, ans + s[ind])
        #     rec(ind + 1, ans)
        # rec(0,"")
        # for i in range(len(temp)):
        #     if isPal(temp[i]):
        #         pal.append(temp[i])
        # l=lambda x:len(x)
        # m=max([len(x) for x in pal])
        # return m
        # pal = []
        # temp = []
        # dp = {}   

        # def isPal(ans):
        #     return ans == ans[::-1]

        # def rec(ind, ans):
        #     if (ind, ans) in dp:
        #         return
        #     dp[(ind, ans)] = True 
        #     if ind == len(s):
        #         temp.append(ans)
        #         return
        #     rec(ind + 1, ans + s[ind])
        #     rec(ind + 1, ans)
        # rec(0, "")
        # for x in temp:
        #     if isPal(x):
        #         pal.append(x)
        # return max(len(x) for x in pal)

        n=len(s)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        r=s[::-1]
        def rec(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==r[j]:
                dp[i][j]=1+rec(i-1,j-1)
                return dp[i][j]
            else:
                dp[i][j]=max(rec(i-1,j),rec(i,j-1))
                return dp[i][j]
        return rec(n-1,n-1)