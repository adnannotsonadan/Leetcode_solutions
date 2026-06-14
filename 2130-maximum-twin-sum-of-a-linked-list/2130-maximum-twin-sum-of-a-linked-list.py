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
        arr=[]
        n=0
        m=0
        temp=head
        while temp:
            arr.append(temp.val)
            n+=1
            temp=temp.next
        i=0
        j=n-1
        while i<j:
            m=max(m,arr[i]+arr[j])
            j-=1
            i+=1
        return m
        