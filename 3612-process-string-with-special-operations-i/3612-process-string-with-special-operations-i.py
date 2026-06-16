class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        for char in s:
            if char.isalpha():
                res+=char
            elif char=='*':
                res=res[:-1]
            elif char=='#':
                res+=res
            elif char=='%':
                res=res[::-1]  
        return res