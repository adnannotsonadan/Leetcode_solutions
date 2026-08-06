class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        st=[]
        for br in s:
            if br in "([{":
                st.append(br)
            elif br in ")]}":
                if not st:
                    return False
                if (br==')' and st[-1]!='(')  or (br==']' and st[-1]!='[') or (br=='}' and st[-1]!='{'):
                    return False
                st.pop()
                
        if not st:
            return True
        return False

        
