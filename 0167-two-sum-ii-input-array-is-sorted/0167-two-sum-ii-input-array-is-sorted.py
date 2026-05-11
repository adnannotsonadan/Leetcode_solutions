class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        i=0
        j=n-1

        while i<j:
            x=numbers[i]+numbers[j]
            if x==target:
                return [i+1,j+1]
            else:
                if x>target:
                    j-=1
                else:
                    i+=1
            