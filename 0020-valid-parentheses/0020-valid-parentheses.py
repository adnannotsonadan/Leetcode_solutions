class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if len(s)<=1:
            return False
        for ch in s:
            if ch in '([{':
                st.append(ch)
            elif ch in ')]}':
                if st:
                    x=st.pop()
                    if x=='(' and ch!=')' or x=='[' and ch!=']' or x=='{' and ch!='}':
                        return False
                else:
                    return False
        if  st:
            return False
        return True
                    