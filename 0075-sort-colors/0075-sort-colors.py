class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=[]
        w=[]
        b=[]

        for num in nums:
            if num==0:
                r.append(num)
            elif num==1:
                w.append(num)
            else:
                b.append(num)
        
        for i in range(len(r)):
            nums[i]=0
        for i in range(len(r),len(w)+len(r)):
            nums[i]=1
        for i in range(len(w)+len(r),len(b)+len(w)+len(r)):
            nums[i]=2
        print(r)
        print(w)
        print(b)