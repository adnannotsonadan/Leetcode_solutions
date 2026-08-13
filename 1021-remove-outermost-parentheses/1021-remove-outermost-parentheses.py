class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp=""
        c=0

        for ch in s:
            if ch=='(':
                c+=1
                if c>1:
                    temp+=ch
            else:
                if ch==')':
                    c-=1
                    if c!=0:
                        temp+=ch

        return temp