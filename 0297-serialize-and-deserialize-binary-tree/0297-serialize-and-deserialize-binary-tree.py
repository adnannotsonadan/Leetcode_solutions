# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def bfs(node,res):
            if not node:
                return 'N'
            q=deque([node])
            while q:
                f=q.popleft()
                if not f:
                    res.append('N')
                    continue
                res.append(str(f.val))
                q.append(f.left)
                q.append(f.right)
            return ",".join(res)
        return bfs(root,res)
          

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def bfs1(data):
            if not data:
                return None
            vals=data.split(',')
            if vals[0]=='N':
                return None
            root=TreeNode(int(vals[0]))
            q=deque([root])
            i=1
            while q and i<len(vals):
                f=q.popleft()
                if i<len(vals) and vals[i] !='N':
                    f.left=TreeNode(int(vals[i]))
                    q.append(f.left)
                i+=1
                if i<len(vals) and vals[i]!='N':
                    f.right=TreeNode(int(vals[i]))
                    q.append(f.right)
                i+=1
            return root
        return bfs1(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))