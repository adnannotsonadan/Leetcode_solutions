class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        s=set(nums)
        maxi=0
        for num in s:
            if num-1 not in s:
                start=num
                count=1
                curr=num
                while curr+1 in s:
                    count+=1
                    curr=curr+1
                maxi=max(maxi,count)
        return maxi
