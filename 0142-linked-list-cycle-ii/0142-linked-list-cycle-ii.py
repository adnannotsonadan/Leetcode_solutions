# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # l=set()
        # temp=head
        # while temp is not None:
        #     if temp not in l:
        #         l.add(temp)
        #         temp=temp.next
        #     elif temp in l:
        #         return temp
        #     else:
        #         return -1
        l=[]
        temp=head
        while temp:
            if temp not in l:
                l.append(temp)
                temp=temp.next
            else:
                return temp
        return None