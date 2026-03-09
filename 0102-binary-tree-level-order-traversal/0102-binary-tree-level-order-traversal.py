# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return []
        def lvl(node):
            q=deque([])
            q.append(root)
            while q:
                lvl_size=len(q)
                curr_lvl=[]
                for i in range(lvl_size):
                    f=q.popleft()
                    curr_lvl.append(f.val)
                    if f.left is not None:
                        q.append(f.left)
                    if f.right is not None:
                        q.append(f.right) 
                res.append(curr_lvl)
        
        lvl(root)
        return res