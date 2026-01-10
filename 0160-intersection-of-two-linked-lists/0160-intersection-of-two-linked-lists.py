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
        temp1=headA
        temp2=headB
        l1={}
        l2={}
        while temp1:
            l1[temp1]=1
            temp1=temp1.next
            
        while temp2:
            if temp2 in l1:
                return temp2
            else:
                temp2=temp2.next
        
