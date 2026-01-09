# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # l=set()
        # temp=head
        # while temp is not None:
        #     if temp not in l:
        #         l.add(temp)
        #         temp=temp.next
        #     else:
        #         return True
        # return False
        l=[]
        temp=head
        while temp:
            if temp not in l:
                l.append(temp)
                temp=temp.next
            else:
                return True
        return False