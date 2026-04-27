# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # USING BFS
        # if not root:
        #     return 0
        # dep=0
        # def lvl(node,dep):
        #     q=deque()
        #     q.append(node)
        #     while q:
        #         dep+=1
        #         for _ in range(len(q)):
        #             f=q.popleft()
        #             if f.left is not None:
        #                 q.append(f.left)
        #             if f.right is not None:
        #                 q.append(f.right)
        #     return dep
        # return lvl(root,dep)

        # USING RECURSION OF DFS

        def solve(node):
            if node==None:
                return 0
            leftheight=solve(node.left)
            rightheight=solve(node.right)
            return 1+max(leftheight,rightheight)
        return solve(root)
        