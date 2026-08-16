class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if not st:
                    return False
                if ch==')' and st[-1]!='(' or ch==']' and st[-1]!='[' or ch=='}' and st[-1]!='{':
                    return False
                else:
                    st.pop()
        if  st:
            return False
        return True