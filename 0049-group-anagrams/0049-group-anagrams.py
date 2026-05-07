class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m={}
        for word in strs:
            x="".join(sorted(word))
            if x not in m:
                m[x]=[word]
            else:
                m[x].append(word)
        ans=[]
        for x in m:
            ans.append(m[x])
        return ans 
                
