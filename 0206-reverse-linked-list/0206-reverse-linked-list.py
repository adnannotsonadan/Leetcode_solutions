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
    # itrrative approach

        # prev=None
        # curr=head
        # while curr:
        #     nxt=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=nxt
        # return prev

    # naive approach
        # l=[]
        # temp=head
        # while temp:
        #     l.append(temp.val)
        #     temp=temp.next
        # l.reverse()
        # temp=head
        # for x in l:
        #     temp.val=x
        #     temp=temp.next
        # return head
    
    # recursive approach
        def rev(prev,curr):
            if curr==None:
                return prev
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            return rev(prev,curr)
        return rev(None,head)
