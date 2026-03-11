class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for i in range(len(s)):
            if s[i] in"([{":
                st.append(s[i])
            else:
                if len(st) == 0 :
                    return False
                if s[i] in ")]}":
                    f=st.pop()
                    if s[i]==')' and f=='(':
                        continue
                    elif s[i]==']' and f=='[':
                        continue
                    elif s[i]=='}' and f=='{':
                        continue
                    else:
                        return False
        if len(st)!=0:
            return False
        return True
                
