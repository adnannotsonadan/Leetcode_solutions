class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m={}
        temp=[]
        n=len(nums)
        for num in nums:
            if num not in m:
                m[num]=1
            else:
                m[num]+=1
        
        for item in m:
            if m[item]>n//3:
                temp.append(item)
        return temp