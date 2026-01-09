# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        temp=head
        l.sort()
        i=0
        while temp:
            temp.val=l[i]
            i+=1
            temp=temp.next
        return head
        
        