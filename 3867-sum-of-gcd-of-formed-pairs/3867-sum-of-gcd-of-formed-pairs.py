from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pre=[]
        mx=float('-inf')
        for num in nums:
            mx=max(mx,num)
            x=math.gcd(num,mx)
            pre.append(x)
        pre.sort()
        
        i=0
        j=len(pre)-1
        ans=0
        while i<j:
            ans+=math.gcd(pre[i],pre[j])
            i+=1
            j-=1
        return ans