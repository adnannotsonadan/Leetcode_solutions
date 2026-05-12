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
        s=set()

        temp=head
        while temp:
            if temp not in s:
                s.add(temp)
            else:
                return True
            temp=temp.next
        return False
        