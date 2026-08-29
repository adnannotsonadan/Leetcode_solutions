class Solution:
    def firstUniqChar(self, s: str) -> int:
        m={}
        s=list(s)
        for ch in s:
            if ch not in m:
                m[ch]=1
            else:
                m[ch]+=1
        x=[]

        for key,val in m.items():
            if val==1:
                x.append(s.index(key))
        if not x:
            return -1
        else:
            return min(x)
        
        