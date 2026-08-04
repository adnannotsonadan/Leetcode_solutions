class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        if not strs:
            return ""
        strs.sort()
        s=strs[0]
        e=strs[-1]
        for i in range(len(s)):
            if s[i]==e[i]:
                res+=s[i]
            else:
                break
        return res