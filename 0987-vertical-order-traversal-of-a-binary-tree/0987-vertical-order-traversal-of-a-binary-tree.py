from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        m=[]
        def dfs(node,col):
            if node is None:
                return
            for i in range(len(m)):
                if m[i][0] == col[0]:
                    m[i].append((col[1],node.val))
                    break
            else:
                m.append([col[0] , (col[1],node.val)])
            # print(m)
            dfs(node.left,(col[0]-1,col[1]+1))
            dfs(node.right,(col[0]+1,col[1]+1))
        dfs(root,(0,0))

        m.sort(key = lambda x:x[0])
        
        for i in range(len(m)):
            m[i] = m[i][1:]
            m[i].sort()
            for j in range(len(m[i])):
                m[i][j] = m[i][j][1]
        return m