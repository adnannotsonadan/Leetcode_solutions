class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res=''
        for word in words:
            s=0
            for i in range(len(word)):
                s+=weights[ord(word[i])-ord('a')]
            x=s%26
            res+=chr(ord('z')-x)
            
        return res
        