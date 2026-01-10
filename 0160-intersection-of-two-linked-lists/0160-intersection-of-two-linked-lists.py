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
        # temp1=headA
        # temp2=headB
        # l1={}
        # l2={}
        # while temp1:
        #     l1[temp1]=1
        #     temp1=temp1.next
            
        # while temp2:
        #     if temp2 in l1:
        #         return temp2
        #     else:
        #         temp2=temp2.next
        # sol2

        temp1=headA
        temp2=headB
        l1=0
        while temp1:
            l1+=1
            temp1=temp1.next
        l2=0
        while temp2:
            l2+=1
            temp2=temp2.next
        diff=abs(l1-l2)

        temp1=headA
        temp2=headB
        if l1>l2:
            while diff!=0:
                diff-=1
                temp1=temp1.next
            while temp1 or temp2:
                if temp1==temp2:
                    return temp1
                else:
                    temp1=temp1.next
                    temp2=temp2.next
            
        elif l2>l1:
            while diff!=0:
                diff-=1
                temp2=temp2.next
            while temp1 or temp2:
                if temp1==temp2:
                    return temp1
                else:
                    temp1=temp1.next
                    temp2=temp2.next
                    
        if l1==l2:
            while temp1 or temp2:
                if temp1==temp2:
                    return temp1
                else:
                    temp1=temp1.next
                    temp2=temp2.next
        return None

