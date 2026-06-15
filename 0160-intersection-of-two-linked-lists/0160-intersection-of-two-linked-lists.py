# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s=set()
        temp=headA
        while temp:
            s.add(temp)
            temp=temp.next
        temp1=headB
        while temp1:
            if temp1 in s:
                return temp1
            temp1=temp1.next
        return None