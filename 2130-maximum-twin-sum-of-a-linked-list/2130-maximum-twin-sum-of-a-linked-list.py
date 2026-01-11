# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        all_sums=[]
        
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        
        n = len(arr)
        max_sum = 0
        
        for i in range(n//2):
            max_sum = max(max_sum, arr[i] + arr[n-1-i])
        
        return max_sum