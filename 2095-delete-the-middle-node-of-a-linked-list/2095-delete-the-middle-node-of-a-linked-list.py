# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=0
        temp=head
        while temp!=None:
            l+=1
            temp=temp.next
        temp=head
        middle=l//2
        if middle == 0:
            return None
        i=middle
        while (i-1)!=0:
            i-=1
            temp=temp.next
        temp.next=temp.next.next
        return head
        
