class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # arr=list(s)
        # temp=[]
        # obs=0
        # for i in range(len(arr)):
        #     if arr[i]=='(':
        #         obs+=1
        #         if obs>1:
        #             temp.append(arr[i])
        #         else:
        #             continue
        #     else:
        #         obs-=1
        #         if obs!=0:
        #             temp.append(arr[i])
        # x="".join(temp)
        # return x
        st=""
        op=0
        cl=0

        for i in range(len(s)):
            if s[i]=='(':
                op+=1
                if op>1:
                    st+=s[i]
            elif s[i]==')':
                cl+=1
                if cl>op:
                    cl=0
                    continue
                elif cl==op:
                    op=0
                    cl=0
                    continue
                else:
                    
                    st+=')'
        return st
            