class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        res=[]
        max_val=max(bulbs)
        hash=[0]*(max_val+1)
        for x in bulbs:
            hash[x]+=1
        for i in range(len(hash)):
            if hash[i]%2==1:
                res.append(i)
        return res