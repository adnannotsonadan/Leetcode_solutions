class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        if len(s)==1:
            return False
        for ch in s:
            
            if ch in '([{':
                st.append(ch)
            else:
                if not st:
                    return False
                e=st.pop()
                if e=='(' and ch!=')' or e=='[' and ch!=']' or e=='{' and ch!='}':
                    return False
        if len(st)!=0:
            return False
        return True

