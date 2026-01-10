# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if head == None or head.next==None:
        #     return head
        # new_node=self.reverseList(head.next)
        # head.next.next=head
        # head.next=None
        # return new_node
    # naive approach
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.reverse()
        temp=head
        for x in l:
            temp.val=x
            temp=temp.next
        return head
        