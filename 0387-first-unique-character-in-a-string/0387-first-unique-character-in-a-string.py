class Solution:
    def firstUniqChar(self, s: str) -> int:
        m={}
        for ch in s:
            if ch not in m:
                m[ch]=1
            else:
                m[ch]+=1
        for key,val in m.items():
            if val==1:
                return s.index(key)
        return -1