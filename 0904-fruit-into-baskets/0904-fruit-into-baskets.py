class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # bf
        # maxi=0
        # n=len(fruits)
        # for i in range(n):
        #     s=set()
        #     c=0
        #     for j in range(i,n):
        #         s.add(fruits[j])
        #         if len(s)>2:
        #             break
        #         c+=1
        #         maxi=max(maxi,c)
        # return maxi

        n=len(fruits)
        l=0
        r=0
        d={}
        maxi=0
        while r<n:
            if fruits[r] not in d:
                d[fruits[r]]=1
            else:
                d[fruits[r]]+=1
            if len(d)>2:
                while len(d)!=2:
                    d[fruits[l]]-=1
                    if d[fruits[l]]==0:
                        d.pop(fruits[l])
                    l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi