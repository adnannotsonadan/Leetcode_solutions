# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1=[]
        while l1:
            temp1.append(str(l1.val))
            l1=l1.next
        temp2=[]
        while l2:
            temp2.append(str(l2.val))
            l2=l2.next
        temp1.reverse()
        temp2.reverse()
        s1 = "".join(temp1)
        s2 = "".join(temp2)
        s1=int(s1)
        s2=int(s2)
        final=s1+s2

        arr=[]
        if final == 0:
           arr.append(0)

        while final!=0:
            ld=final%10
            arr.append(ld)
            final//=10
        # arr.reverse()

        new_node=ListNode(0)
        temp=new_node
        for x in arr:
            temp.next=ListNode(x)
            temp=temp.next
        return new_node.next
        